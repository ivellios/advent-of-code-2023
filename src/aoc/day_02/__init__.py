from dataclasses import dataclass

from aoc.base import BaseChallenge


class GameLimit:
    red = 12
    green = 13
    blue = 14


class GameSet:
    red: int
    green: int
    blue: int

    def __init__(self, data):
        self.red = 0
        self.green = 0
        self.blue = 0

        for cubes_data in data.split(", "):
            amount, color = cubes_data.split(" ")
            amount = int(amount)
            setattr(self, color, amount)

    def is_possible(self):
        return all(
            [
                self.red <= GameLimit.red,
                self.green <= GameLimit.green,
                self.blue <= GameLimit.blue,
            ]
        )

    def has_red(self):
        return self.red > 0

    def has_green(self):
        return self.green > 0

    def has_blue(self):
        return self.blue > 0


class Game:
    def __init__(self, input_data):
        game, rest = input_data.split(": ")
        self.id = int(game.split(" ")[1])
        self.sets: list[GameSet] = [GameSet(data) for data in rest.split("; ")]

    def is_possible(self) -> bool:
        return all([cube_set.is_possible() for cube_set in self.sets])

    @property
    def max_red(self):
        return max([cube_set.red for cube_set in self.sets])

    @property
    def max_green(self):
        return max([cube_set.green for cube_set in self.sets])

    @property
    def max_blue(self):
        return max([cube_set.blue for cube_set in self.sets])

    @property
    def power(self):
        return self.max_red * self.max_green * self.max_blue


class Challenge(BaseChallenge):
    def part_1(self):
        possible_games = []
        for game in self.input_lines():
            game_o = Game(game)
            if game_o.is_possible():
                possible_games.append(game_o.id)

        return sum(possible_games)

    def part_2(self):
        total_power = 0
        for game in self.input_lines():
            game_o = Game(game)
            total_power += game_o.power

        return total_power


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
