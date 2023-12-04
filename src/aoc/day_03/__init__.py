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

    def part_1(self):
        counted_numbers = 0
        for line_idx, line in enumerate(self.input_lines()):
            numbers = find_all_numbers_in_string(line)
            ic(numbers)
            for index, number in numbers.items():

                start = index - 1
                end = index + len(number) + 1

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
                    partial_line_before = self.input_lines()[line_idx-1][start:end]
                else:
                    partial_line_before = ""

                if line_after_index < len(self.input_lines()):
                    partial_line_after = self.input_lines()[line_idx+1][start:end]
                else:
                    partial_line_after = ""
                #
                #
                # ic(
                #     number,
                #     len(number),
                #     char_before,
                #     char_after,
                #     partial_line_before,
                #     partial_line_after
                # )

                if char_before and char_before not in self.excluded_chars:
                    counted_numbers += int(number)
                    continue

                if char_after and char_after not in self.excluded_chars:
                    counted_numbers += int(number)
                    continue

                if any(char not in self.excluded_chars for char in partial_line_before):
                    counted_numbers += int(number)
                    continue

                if any(char not in self.excluded_chars for char in partial_line_after):
                    counted_numbers += int(number)
                    continue

        return counted_numbers

    def part_2(self):
        return


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
