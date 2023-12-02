from aoc.base import BaseTestChallenge

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (142, 281)
    expected_results_from_real_data = (54990, 54473)

    def test_on_sample_data_part_1(self):
        challenge = self.challenge_class()
        challenge._input_lines = [
            line.strip()
            for line in """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """.split("\n")
            if line.strip() != ""
        ]

        assert challenge.part_1() == 142
