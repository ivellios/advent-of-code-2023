from functools import reduce

from icecream import ic

from aoc.base import BaseChallenge


class MapVector:
    def __init__(self, source, range_length, destination):
        self.source = source
        self.range_length = range_length
        self.destination = destination

    @property
    def shift(self):
        return self.destination - self.source

    @property
    def range_limit(self):
        return self.source + self.range_length

    def is_in_range(self, value):
        return 0 <= value - self.source < self.range_length

    def map(self, value):
        return value + self.shift

    def __lt__(self, other):
        return self.source < other.source


class Mapper:
    def __init__(self, input_data: list[str]):
        self.vectors = []
        for data in input_data:
            destination, source, range_length = data.split(" ")
            self.vectors.append(
                MapVector(int(source), int(range_length), int(destination))
            )

        self.vectors.sort()

    def map(self, seed):
        for vector in self.vectors:
            if vector.is_in_range(seed):
                return vector.map(seed)
        return seed


class Challenge(BaseChallenge):
    def part_1(self):
        seeds = [int(value.strip()) for value in self.input_lines()[0].split(":")[1].split(" ") if value.strip() != ""]

        map_indexes = []
        for idx, line in enumerate(self.input_lines()):
            if line.strip() == "":
                map_indexes.append(idx)
        map_indexes.append(idx+1)

        mappers = []

        for mapper_idx in range(0, 7):
            mappers.append(
                Mapper(
                    self.input_lines()[map_indexes[mapper_idx]+2:map_indexes[mapper_idx+1]]
                )
            )

        return min(reduce(lambda x, mapper: mapper.map(x), mappers, seed) for seed in seeds)

    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
