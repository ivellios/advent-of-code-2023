import pytest

from aoc.base import BaseTestChallenge
from . import Challenge, Pathfinder


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (374, 82000210)
    expected_results_from_real_data = (9605127, 458191688761)

    @pytest.mark.parametrize(
        "x, y, used_cols, used_rows, expected",
        (
            ((0, 0), (1, 1), [0, 1], [0, 1], 2),
            ((1, 1), (2, 2), [1, 2], [1, 2], 2),
            ((1, 1), (0, 0), [0, 1], [0, 1], 2),
            ((0, 0), (2, 2), [0, 1, 2], [0, 1, 2], 4),
            ((5, 5), (5, 8), [5, 6, 7, 8], [5, 6, 7, 8], 3),
            ((8, 5), (5, 5), [5, 6, 7, 8], [5, 6, 7, 8], 3),
            ((5, 5), (5, 8), [5, 7, 8], [5, 6, 7, 8], 3),  # double col but unaffected
            ((8, 5), (5, 5), [5, 6, 7, 8], [5, 7, 8], 3),  # double row but unaffected
            ((5, 5), (5, 8), [5, 6, 7, 8], [5, 7, 8], 4),  # double row
            ((8, 5), (5, 5), [5, 7, 8], [5, 6, 7, 8], 4),  # double col
        ),
    )
    def test_get_shortest_path_unused_cols_rows(
        self, x, y, used_cols, used_rows, expected
    ):
        pf = Pathfinder([x, y], used_cols, used_rows)
        pf.used_rows = used_rows
        pf.used_cols = used_cols
        assert pf.get_shortest_path(x, y) == expected

    def test_on_sample_data_part_2_example1(self):
        test_input = """
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
        """.split(
            "\n"
        )

        c = Challenge()
        c._input_lines = test_input

        assert c.part_2(10) == 1030

    def test_on_sample_data_part_2_example2(self):
        test_input = """
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
        """.split(
            "\n"
        )

        c = Challenge()
        c._input_lines = test_input

        assert c.part_2(100) == 8410
