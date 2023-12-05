from collections import defaultdict
from functools import reduce
from operator import mul

from icecream import ic

from aoc.base import BaseChallenge


def find_all_numbers_in_string(value) -> dict[int, str]:
    """
    Returns a dict of positions where each number starts as keys
    and the numbers themselves as values.
    """
    numbers = {}
    number = ""
    for idx, char in enumerate(value):
        if char.isdigit():
            number += char
        elif number:
            numbers[idx - len(number)] = number
            number = ""
    if number:
        numbers[len(value) - len(number)] = number
    return numbers


class Challenge(BaseChallenge):

    special_chars = "!@#$%^&*()-+=_~`/\\"
    excluded_chars = ".0123456789"

    def extract_data(self, index, number, line_idx, line):

        start = index - 1
        end = index + len(number)  # + 1

        if index == 0:
            start = 0
            char_before = ""
        else:
            char_before = line[index - 1]

        if index + len(number) == len(line):
            end = index + len(number) - 1
            char_after = ""
        else:
            char_after = line[index + len(number)]

        line_before_index = line_idx - 1
        line_after_index = line_idx + 1

        if line_before_index >= 0:
            partial_line_before = self.input_lines()[line_idx - 1][start : end + 1]
        else:
            partial_line_before = ""

        if line_after_index < len(self.input_lines()):
            partial_line_after = self.input_lines()[line_idx + 1][start : end + 1]
        else:
            partial_line_after = ""

        return (
            start,
            end,
            char_before,
            char_after,
            partial_line_before,
            partial_line_after,
        )

    @staticmethod
    def part_1_count(
        counted_numbers,
        line_idx,
        number,
        start,
        end,
        char_before,
        char_after,
        partial_line_before,
        partial_line_after,
    ):
        if char_before and char_before not in Challenge.excluded_chars:
            counted_numbers.append(int(number))
            return

        if char_after and char_after not in Challenge.excluded_chars:
            counted_numbers.append(int(number))
            return

        if any(char not in Challenge.excluded_chars for char in partial_line_before):
            counted_numbers.append(int(number))
            return

        if any(char not in Challenge.excluded_chars for char in partial_line_after):
            counted_numbers.append(int(number))
            return

    @staticmethod
    def part_1_aggregator(counted_numbers):
        return sum(counted_numbers)

    @staticmethod
    def part_2_count(
        counted_numbers,
        line_idx,
        number,
        start,
        end,
        char_before,
        char_after,
        partial_line_before,
        partial_line_after,
    ):
        if char_before == "*":
            counted_numbers[(line_idx, start)].append(int(number))
            return

        if char_after == "*":
            counted_numbers[(line_idx, end)].append(int(number))
            return

        should_continue = False
        for idx, char in enumerate(partial_line_before):
            if char == "*":
                counted_numbers[(line_idx - 1, start + idx)].append(int(number))
                should_continue = True
                break
        if should_continue:
            ic("continue")
            return

        for idx, char in enumerate(partial_line_after):
            if char == "*":
                counted_numbers[(line_idx + 1, start + idx)].append(int(number))
                ic("break")
                break

    @staticmethod
    def part_2_aggregator(counter_numbers):
        return sum(reduce(mul, l) for l in counter_numbers.values() if len(l) > 1)

    def process_part(self, counted_numbers, count_function, aggregator_function):
        for line_idx, line in enumerate(self.input_lines()):
            numbers = find_all_numbers_in_string(line)

            for index, number in numbers.items():
                count_function(
                    counted_numbers,
                    line_idx,
                    number,
                    *self.extract_data(index, number, line_idx, line)
                )

        return aggregator_function(counted_numbers)

    def part_1(self):
        counted_numbers = []
        return self.process_part(
            counted_numbers, self.part_1_count, self.part_1_aggregator
        )

    def part_2(self):
        counted_numbers: dict[tuple[int, int], list[int]] = defaultdict(list)
        return self.process_part(
            counted_numbers, self.part_2_count, self.part_2_aggregator
        )


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
