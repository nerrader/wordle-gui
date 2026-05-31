from httpx import Client as httpx_client

from wordle_gui import constants as const
from wordle_gui import cache
from wordle_gui import nyt


def guessing_loop(wordle_solution: str, valid_guesses: set[str]) -> None:
    attempts = 0
    while attempts < 6:
        guess = input(f"Guess {attempts + 1}/6: ").lower().strip()
        print(f"You guessed: {guess}")

        if guess not in valid_guesses:
            print("Invalid guess. Please enter a valid 5-letter word.")
            continue

        if guess == wordle_solution:
            print(
                f"Congratulations! You've guessed the wordle in {attempts + 1} tr{'ies' if attempts + 1 != 1 else 'y'}!"
            )
            return

        print("Incorrect guess. Try again.")
        attempts += 1


def main() -> None:
    const.CACHE_DIR_PATH.mkdir(parents=True, exist_ok=True)
    with httpx_client(timeout=10.0, headers={"User-Agent": const.USER_AGENT}) as client:
        cache.sync_cache("possible_solutions", const.CACHE_DIR_PATH, client)
        cache.sync_cache("valid_guesses", const.CACHE_DIR_PATH, client)

    possible_solutions_set: set[str] = cache.read_cache(
        "possible_solutions", const.CACHE_DIR_PATH
    )
    valid_guesses: set[str] = cache.read_cache("valid_guesses", const.CACHE_DIR_PATH)
    all_allowed_words = possible_solutions_set | valid_guesses

    wordle_solution = nyt.fetch_wordle_solution(const.USER_AGENT)
    guessing_loop(wordle_solution, all_allowed_words)


if __name__ == "__main__":
    main()
