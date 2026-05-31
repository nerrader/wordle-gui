from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx
    from pathlib import Path


def validate_filename_base(filename_base: str) -> None:
    """Checks the filename base and raises and error if invalid.
    Only 'possible_solutions' and 'valid_guesses' are valid filename bases."""
    if filename_base not in ["possible_solutions", "valid_guesses"]:
        raise ValueError(f"Invalid filename base: {filename_base}")


def sync_cache(filename_base: str, cache_dir: Path, client: httpx.Client) -> None:
    """Fetches data from the github repository, and saves it to cache. Checks ETAG to prevent uneccessary saving.

    Args:
        - filename_base (str): Can only be "possible_solutions" or "valid_guesses",
        as those are the only two types of cache used in this application currently.
        - client (httpx.Client | None, optional): The HTTPX client to use for the request.
        If None, a new client will be created for this request. Defaults to None.
        - cache_dir (Path): The directory where the cache files are stored.
    """

    validate_filename_base(filename_base)
    try:
        request_headers: dict[str, str] = (
            {"If-None-Match": (cache_dir / f"{filename_base}.etag").read_text().strip()}
            if (cache_dir / f"{filename_base}.etag").exists()
            else {}
        )
        response = client.get(
            f"https://raw.githubusercontent.com/nerrader/wordle-gui/refs/heads/main/data/{filename_base}.txt",
            headers=request_headers,
        )
        if response.status_code == 304:
            print(f"Cache for {filename_base} is up to date.")
            return
        elif response.status_code != 200:
            raise httpx.HTTPStatusError(
                f"Failed to fetch {filename_base} cache. Status code: {response.status_code}",
                request=response.request,
                response=response,
            )

        (cache_dir / f"{filename_base}.txt").write_text(response.text)
        if response.headers.get("ETag"):
            (cache_dir / f"{filename_base}.etag").write_text(response.headers["ETag"])
        print(f"Cache for {filename_base} downloaded and saved.")

    except Exception as error:
        print(f"An error occurred while fetching {filename_base}: {error}")


def read_cache(filename_base: str, cache_dir: Path) -> set[str]:
    """Reads the cache file and returns a set of words.

    Args:
        filename_base (str): Can only be "possible_solutions" or "valid_guesses",
        as those are the only two types of cache used in this application currently.
        cache_dir (Path): The directory where the cache files are stored.

    Raises:
        ValueError: If the filename_base is invalid.
        FileNotFoundError: If the cache file does not exist.
    """
    validate_filename_base(filename_base)

    cache_file = cache_dir / f"{filename_base}.txt"
    if not cache_file.exists():
        raise FileNotFoundError(f"Cache file for {filename_base} not found.")

    return set(cache_file.read_text().splitlines())
