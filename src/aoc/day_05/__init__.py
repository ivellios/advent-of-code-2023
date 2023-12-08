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

    @property
    def start(self):
        return self.source

    end = range_limit

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


class RangesMapper(Mapper):
    def map(self, params_ranges: list[range]) -> list[range]:
        ranges = []
        ranges_lengths = []
        for the_range in params_ranges:
            # ic("New range...")
            range_start = the_range[0]
            range_end = the_range[-1]
            range_length = range_end - range_start
            # ic(range_start, range_end, range_length)

            for vidx, vector in enumerate(self.vectors):
                # ic("Processing vector...")
                # ic(vector.destination, vector.source, vector.range_length)
                # ic(vector.start, vector.end, vector.shift)

                if vidx == 0 and vector.start > range_start:
                    ranges.append(range(range_start, vector.start))
                    ranges_lengths.append(vector.start - range_start)

                # ic("Fetching intersection min...")
                vector_range_start = max(range_start, vector.start) # min(vector_common_set)
                # ic("Fetching intersection max...")
                vector_range_end = min(range_end, vector.end)  # max(vector_common_set)

                if vector_range_end > vector_range_start:
                    # ic("Adding range...")
                    ranges.append(
                        range(vector_range_start+vector.shift, vector_range_end+vector.shift+1)
                    )
                    ranges_lengths.append(vector_range_end - vector_range_start)

            if range_end > vector.end:

                if range_start > vector.end:
                    ranges.append(
                        range(range_start, range_end+1)
                    )
                    ranges_lengths.append(range_end - range_start)
                else:
                    ranges.append(
                        range(vector.end+1, range_end+1)
                    )
                    ranges_lengths.append(range_end - vector.end)

            # ic(ranges, ranges_lengths)

        return ranges


class Challenge(BaseChallenge):

    def get_mappers(self, mapper_klass):
        map_indexes = []
        for idx, line in enumerate(self.input_lines()):
            if line.strip() == "":
                map_indexes.append(idx)
        map_indexes.append(idx+1)

        return [
            mapper_klass(
                self.input_lines()[map_indexes[mapper_idx]+2:map_indexes[mapper_idx+1]]
            )
            for mapper_idx in range(0, 7)
        ]

    def part_1(self):
        seeds = [int(value.strip()) for value in self.input_lines()[0].split(":")[1].split(" ") if value.strip() != ""]

        mappers = self.get_mappers(Mapper)
        return min(reduce(lambda x, mapper: mapper.map(x), mappers, seed) for seed in seeds)

    def part_2(self):
        seeds_line = [
            int(value.strip()) for value in self.input_lines()[0].split(":")[1].split(" ") if value.strip() != ""
        ]

        seeds = zip(seeds_line[::2], seeds_line[1::2])
        mappers = self.get_mappers(RangesMapper)

        values = []
        for seed_range_start, seed_range in seeds:
            values.append(
                reduce(
                    lambda x, mapper: mapper.map(x),
                    mappers,
                    [range(seed_range_start, seed_range_start + seed_range)]
                )
            )

        vals = []
        for ranges_list in values:
            vals += [
                rng[0]
                for rng in ranges_list
            ]

        return min(vals)


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
