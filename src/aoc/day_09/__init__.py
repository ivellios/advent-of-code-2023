from functools import reduce

from icecream import ic  # type: ignore

from aoc.base import BaseChallenge


ic.disable()


class HistoryProcessor:

    def __init__(self, data, store_num_func: callable, reduce_func: callable):
        self.store_num_func = store_num_func
        self.reduce_function = reduce_func
        self.data = data

    def process(self) -> int:
        sums = 0
        for line in self.data:
            sums += self.process_line([int(val.strip()) for val in line.split(" ") if val.strip() != ""])
        return sums

    @staticmethod
    def process_differences(numbers: list[int]) -> list[int]:
        res_nums = []
        for idx, number in enumerate(numbers):
            if idx == len(numbers) - 1:
                break
            res_nums.append(numbers[idx + 1] - numbers[idx])

        return res_nums

    def process_line(self, numbers: list[int]) -> int:
        stored_nums = []
        while any(n != 0 for n in numbers):
            res_nums = self.process_differences(numbers)
            stored_nums.append(self.store_num_func(numbers))
            numbers = res_nums

        return reduce(self.reduce_function, reversed(stored_nums), 0)


class Challenge(BaseChallenge):

    def part_1(self):
        return HistoryProcessor(
            self.input_lines(),
            lambda numbers: numbers.pop(),
            lambda a,b: a+b
        ).process()


    def part_2(self):
        return HistoryProcessor(
            self.input_lines(),
            lambda numbers: numbers[0],
            lambda a, b: b - a
        ).process()


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
