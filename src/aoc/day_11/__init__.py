import time

from icecream import ic  # type: ignore

from aoc.base import BaseChallenge


ic.disable()


class Pathfinder:
    def __init__(
        self,
        galaxies: list[tuple[int, int]],
        used_cols: set[int],
        used_rows: set[int],
        cols_expanse=1,
        rows_expanse=1,
    ):
        self.galaxies = galaxies
        self.used_cols = used_cols
        self.used_rows = used_rows
        self.cols_expanse = cols_expanse
        self.rows_expanse = rows_expanse

    def get_shortest_path(self, x: tuple[int, int], y: tuple[int, int]):
        dest_col = abs(y[0] - x[0])
        dest_row = abs(y[1] - x[1])
        distance = dest_col + dest_row

        ic("Checking used cols")
        cols_range = range(x[0], y[0]) if x[0] < y[0] else range(y[0], x[0])
        distance += sum(
            self.cols_expanse for col in cols_range if col not in self.used_cols
        )

        ic("Checking used rows")
        rows_range = range(x[1], y[1]) if x[1] < y[1] else range(y[1], x[1])
        distance += sum(
            self.rows_expanse for row in rows_range if row not in self.used_rows
        )

        return distance

    def find_paths(self):
        distance = 0
        for gidx, galaxy in enumerate(self.galaxies):
            for galaxy2 in self.galaxies[gidx:]:
                ic(galaxy, galaxy2)
                start = time.time_ns()
                distance += self.get_shortest_path(galaxy, galaxy2)
                ic(time.time_ns() - start)
        return distance


class Challenge(BaseChallenge):
    def get_data(self) -> tuple[list[tuple[int, int]], set[int], set[int]]:
        galaxies = []
        used_cols = set()
        used_rows = set()
        for row, line in enumerate(self.input_lines()):
            galaxy_in_row = False
            for col, char in enumerate(line):
                if char == "#":
                    galaxies.append((col, row))
                    used_cols.add(col)
                    galaxy_in_row = True
            if galaxy_in_row:
                used_rows.add(row)

        return galaxies, used_cols, used_rows

    def part_1(self):
        galaxies, used_cols, used_rows = self.get_data()
        ic(galaxies, used_cols, used_rows)
        pf = Pathfinder(galaxies, used_cols, used_rows)
        return pf.find_paths()

    def part_2(self, expanse=1000000):
        galaxies, used_cols, used_rows = self.get_data()
        ic(galaxies, used_cols, used_rows)
        pf = Pathfinder(
            galaxies,
            used_cols,
            used_rows,
            cols_expanse=expanse - 1,
            rows_expanse=expanse - 1,
        )
        return pf.find_paths()


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
