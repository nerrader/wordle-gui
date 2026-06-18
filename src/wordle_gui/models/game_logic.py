from wordle_gui.models import cache
from wordle_gui import constants as const
from wordle_gui.models import nyt


class WordeeGame:
    def __init__(self, target_word=None):
        self._target_word: str = target_word or nyt.fetch_wordle_solution(
            const.USER_AGENT
        )
        self._target_word = self._target_word.lower()
        self._guesses_left: int = 6
        self._game_state: str = "playing"  # should only be playing, win, or loss

    @property
    def target_word(self) -> str:
        return self._target_word

    @property
    def guesses_left(self) -> int:
        return self._guesses_left

    @property
    def game_state(self) -> str:
        return self._game_state

    def get_color_feedback(self, guess: str) -> list[str]:
        guess = guess.lower()
        words_in_target_word = set(self.target_word)

        color_feedback: list[str] = []
        for index, letter in enumerate(guess):
            target_word_letter = self.target_word[index]

            if letter == target_word_letter:
                color_feedback.append("green")
            elif letter in words_in_target_word:
                color_feedback.append("yellow")
                words_in_target_word.remove(letter)
            else:
                color_feedback.append("gray")

        return color_feedback

    def submit_guess(self, guess: str) -> None:
        guess = guess.lower()
        all_valid_guesses = cache.read_cache(
            "valid_guesses", const.CACHE_DIR_PATH
        ) | cache.read_cache("possible_solutions", const.CACHE_DIR_PATH)

        if guess not in all_valid_guesses:
            raise ValueError(f"This guess is not valid: {guess}")
        self._guesses_left -= 1

        if (guess != self.target_word) and self.guesses_left <= 0:
            self._game_state = "loss"
        else:
            self._game_state = "win"
