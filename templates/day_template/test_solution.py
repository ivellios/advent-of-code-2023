from aoc.base import BaseTestChallenge

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (0, 0)
    expected_results_from_real_data = (0, 0)
