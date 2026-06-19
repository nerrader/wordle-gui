import sys

# from httpx import Client as httpx_client
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

# from wordle_gui import constants as const
# from wordle_gui.models import cache
# from wordle_gui.models import nyt

from wordle_gui.views.main_window import MainWindow
from wordle_gui import constants as const


def main() -> None:
    # const.CACHE_DIR_PATH.mkdir(parents=True, exist_ok=True)

    # with httpx_client(timeout=10.0, headers={"User-Agent": const.USER_AGENT}) as client:
    #     cache.sync_cache("possible_solutions", const.CACHE_DIR_PATH, client)
    #     cache.sync_cache("valid_guesses", const.CACHE_DIR_PATH, client)

    # possible_solutions_set: set[str] = cache.read_cache(
    #     "possible_solutions", const.CACHE_DIR_PATH
    # )
    # valid_guesses: set[str] = cache.read_cache("valid_guesses", const.CACHE_DIR_PATH)
    # all_allowed_words = possible_solutions_set | valid_guesses

    # wordle_solution = nyt.fetch_wordle_solution(const.USER_AGENT)
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(
        str(const.SCRIPT_DIR / "assets" / "fonts" / "RobotoMono.ttf")
    )
    app.setStyleSheet((const.ASSETS_DIR_PATH / "style.qss").read_text())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
