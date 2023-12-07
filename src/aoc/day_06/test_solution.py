import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (288, 71503)
    expected_results_from_real_data = (None, None)
