from collections import defaultdict

from icecream import ic

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):


    @staticmethod
    def get_common_numbers_count(line):
        _, cards = line.split(":")
        winning_numbers_card, card = cards.split("|")
        winning_numbers = set(
            [no.strip() for no in winning_numbers_card.split(" ") if no.strip() != ""])
        card_numbers = set([no.strip() for no in card.split(" ") if no.strip() != ""])
        common_numbers = winning_numbers.intersection(card_numbers)
        return len(common_numbers)


    def part_1(self):
        total = 0
        for line in self.input_lines():
            common_numbers_count = self.get_common_numbers_count(line)

            if common_numbers_count:
                total += pow(2, common_numbers_count - 1)

        return total

    def part_2(self):
        copies: dict[int, int] = defaultdict(lambda: 0)
        lines_count = 0
        for idx, line in enumerate(self.input_lines()):
            common_numbers_count = self.get_common_numbers_count(line)

            copies[idx] += 1
            for x in range(common_numbers_count):
                copies[idx+x+1] += copies[idx]
            lines_count += 1

        return sum(list(copies.values())[:lines_count])


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
