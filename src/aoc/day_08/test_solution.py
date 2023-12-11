import pytest

from aoc.base import BaseTestChallenge
from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (6, None)
    expected_results_from_real_data = (None, None)

    def test_on_sample_data_part_1_a(self):
        challenge = self.challenge_class()
        challenge._input_lines = [
            line.strip()
            for line in """RL
            
            AAA = (BBB, CCC)
            BBB = (DDD, EEE)
            CCC = (ZZZ, GGG)
            DDD = (DDD, DDD)
            EEE = (EEE, EEE)
            GGG = (GGG, GGG)
            ZZZ = (ZZZ, ZZZ)""".split(
                "\n"
            )
        ]

        assert challenge.part_1() == 2

    def test_on_sample_data_part_2(self):
        challenge = self.challenge_class()
        challenge._input_lines = [
            line.strip()
            for line in """LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)""".split(
                "\n"
            )
        ]

        assert challenge.part_2() == 6
