import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (4361, 467835)
    expected_results_from_real_data = (538046, 81709807)
