from datetime import date
from typing import Any, TYPE_CHECKING

import httpx
from platformdirs import PlatformDirs

if TYPE_CHECKING:
    from pathlib import Path

_dirs = PlatformDirs("wordle", appauthor="nerrader")
MAIN_DATA_PATH: Path = _dirs.user_data_path
CACHE_DIR_PATH: Path = MAIN_DATA_PATH / "cache"


def guessing_loop(wordle_solution: str) -> None:
    for i in range(1, 7):
        guess = input(f"Guess {i}/6: ").lower().strip()
        print(f"You guessed: {guess}")

        if guess == wordle_solution:
            print(
                f"Congratulations! You've guessed the wordle in {i} tr{'ies' if i != 1 else 'y'}!"
            )
            return

        print("Incorrect guess. Try again.")


def main() -> None:

    current_date = date.today()
    response = httpx.get(f"https://www.nytimes.com/svc/wordle/v2/{current_date}.json")
    data: dict[str, Any] = response.json()

    wordle_solution: str = data["solution"]
    guessing_loop(wordle_solution)


if __name__ == "__main__":
    main()
