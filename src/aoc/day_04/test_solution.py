import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (13, 30)
    expected_results_from_real_data = (23441, 5923918)
