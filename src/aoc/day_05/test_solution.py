import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (35, 46)
    expected_results_from_real_data = (51580674, None)
