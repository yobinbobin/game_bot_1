"""Offline tests for the pure game rules; no Telegram token is needed."""
import unittest
from unittest.mock import patch

from services.services import get_bot_choice, get_winner
from lexicon.lexicon import lexicon_ru


class TestGameRules(unittest.TestCase):
    def test_draws(self):
        for key in ("rock", "paper", "scissors"):
            with self.subTest(move=key):
                self.assertEqual(get_winner(lexicon_ru[key], key), "nobody_won")

    def test_user_wins(self):
        for user, bot in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
            with self.subTest(user=user, bot=bot):
                self.assertEqual(get_winner(lexicon_ru[user], bot), "user_won")

    def test_bot_wins(self):
        for user, bot in (("rock", "paper"), ("paper", "scissors"), ("scissors", "rock")):
            with self.subTest(user=user, bot=bot):
                self.assertEqual(get_winner(lexicon_ru[user], bot), "bot_won")

    def test_bot_returns_known_choice(self):
        with patch("services.services.random.choice", return_value="rock"):
            self.assertEqual(get_bot_choice(), "rock")


if __name__ == "__main__":
    unittest.main()
