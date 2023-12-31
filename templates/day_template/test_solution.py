import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


@pytest.mark.skip
class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (None, None)
    expected_results_from_real_data = (None, None)
