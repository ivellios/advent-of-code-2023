import re
from collections import defaultdict
from typing import Self

from icecream import ic  # type: ignore

from aoc.base import BaseChallenge


class Hand:
    FIGURE_MAPPING = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.strength = self.get_strength()

    def get_types(self) -> defaultdict[str, int]:
        figures: defaultdict = defaultdict(int)
        for i in self.cards:
            figures[i] += 1
        return figures

    @classmethod
    def get_figure(cls, figure: str) -> int:
        return int(cls.FIGURE_MAPPING.get(figure, figure))

    def get_strength(self) -> int:
        types = self.get_types()
        if any([i == 5 for i in types.values()]):
            return 7  # five of a kind
        if any([i == 4 for i in types.values()]):
            return 6  # four of a kind
        if any([i == 3 for i in types.values()]) and any(
            [i == 2 for i in types.values()]
        ):
            return 5  # full house
        if any([i == 3 for i in types.values()]):
            return 4  # three of a kind
        if len(list(i for i in types.values() if i == 2)) == 2:
            return 3  # two pairs
        if any(i == 2 for i in types.values()):
            return 2  # one pair
        return 1  # high card

    def __lt__(self, other: Self):
        if self.strength == other.strength:
            for i in range(5):
                if self.get_figure(self.cards[i]) == self.get_figure(other.cards[i]):
                    continue
                return self.get_figure(self.cards[i]) < self.get_figure(other.cards[i])
        return self.strength < other.strength

    def __repr__(self):
        return f"{self.cards} ({self.strength})"


class JokerHand(Hand):
    FIGURE_MAPPING = {
        "J": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def get_types(self) -> defaultdict[str, int]:
        figures = super().get_types()

        for figure in self.FIGURE_MAPPING:
            if figure not in figures:
                figures[figure] = 0

        js = len([_.start() for _ in re.finditer("J", self.cards)])
        for k, v in figures.items():
            if k != "J":
                figures[k] += js

        return figures

    def get_strength(self) -> int:
        types = self.get_types()
        if any([i == 5 for i in types.values()]):
            return 7  # five of a kind
        if any([i == 4 for i in types.values()]):
            return 6  # four of a kind
        if types["J"] == 1 and len([i for i in types.values() if i == 3]) == 2:
            return 5  # full house
        if (
            types["J"] == 0
            and any([i == 3 for i in types.values()])
            and any([i == 2 for i in types.values()])
        ):
            return 5  # full house
        if any([i == 3 for i in types.values()]):
            return 4  # three of a kind
        if types["J"] == 0 and len(list(i for i in types.values() if i == 2)) == 2:
            return 3  # two pairs
        if any(i == 2 for i in types.values()):
            return 2  # one pair
        return 1  # high card


class Challenge(BaseChallenge):
    def part_1(self):
        hands = []
        for i in self.input_lines():
            cards, bid = i.split(" ")
            hands.append(Hand(cards, int(bid)))

        hands.sort()
        return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))

    def part_2(self):
        hands = []
        for i in self.input_lines():
            cards, bid = i.split(" ")
            hands.append(JokerHand(cards, int(bid)))

        hands.sort()
        return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
