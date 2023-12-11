import math

from icecream import ic  # type: ignore

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    directions: str = ""
    mappings: dict = dict()

    def load_maps(self):
        self.directions = self.input_lines()[0]

        self.mappings = {}
        for line in self.input_lines()[2:]:
            _from, _to = line.split(" = ")
            self.mappings[_from] = _to.strip("( )").split(", ")

    def find_route_length(self, start, end_check_function):
        iterator = 0
        idx = start
        while not end_check_function(idx):
            if self.directions[(iterator % len(self.directions))] == "L":
                # ic("L", iterator, idx, self.mappings[idx][0])
                idx = self.mappings[idx][0]
            elif self.directions[(iterator % len(self.directions))] == "R":
                # ic("R", iterator, idx, self.mappings[idx][1])
                idx = self.mappings[idx][1]
            iterator += 1

        return iterator

    def part_1(self):
        self.load_maps()
        return self.find_route_length("AAA", lambda idx: idx == "ZZZ")

    def part_2(self):
        self.load_maps()

        starting_points = {
            point: point for point in self.mappings if point[2].endswith("A")
        }

        for point in starting_points:
            starting_points[point] = self.find_route_length(
                point, lambda idx: idx.endswith("Z")
            )

        return math.lcm(*starting_points.values())


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
