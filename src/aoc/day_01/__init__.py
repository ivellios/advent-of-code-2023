from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    def part_1(self):
        total = 0
        for line in self.input_lines():
            for first in line:
                try:
                    int(first)
                    break
                except ValueError:
                    pass
            for last in reversed(line):
                try:
                    int(last)
                    break
                except ValueError:
                    pass
            total += int(f"{first}{last}")
        return total

    def part_2(self):
        total = 0

        replacements = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        for line in self.input_lines():
            first_pos = None
            last_pos = None
            first_num = None
            last_num = None

            for index, first in enumerate(line):
                try:
                    int(first)
                    first_pos = index
                    first_num = first
                    break
                except ValueError:
                    pass
            for index, last in enumerate(reversed(line)):
                try:
                    int(last)
                    last_pos = len(line) - index - 1
                    last_num = last
                    break
                except ValueError:
                    pass

            for key, value in replacements.items():
                found = line.find(key)
                if found > -1 and (first_pos is None or found < first_pos):
                    first_pos = found
                    first_num = value

            start = last_pos - 1 if last_pos else 0
            restart = True
            while restart:
                for key, value in replacements.items():
                    found = line.find(key, start)
                    if found > -1 and (last_pos is None or found > last_pos):
                        last_pos = found
                        last_num = value
                        start = found + 1
                        break
                else:
                    restart = False

            number = int(f"{first_num}{last_num}")

            total += number
        return total


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
