from platformdirs import PlatformDirs
from pathlib import Path

_dirs = PlatformDirs("wordle", appauthor="nerrader")
MAIN_DATA_PATH: Path = _dirs.user_data_path
CACHE_DIR_PATH: Path = MAIN_DATA_PATH / "cache"

USER_AGENT = "WordleGUI (https://github.com/nerrader/wordle-gui)"
SOLUTIONS_CACHE_PATH = CACHE_DIR_PATH / "possible_solutions.txt"
