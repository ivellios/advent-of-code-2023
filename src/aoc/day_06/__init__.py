from icecream import ic  # type: ignore

from aoc.base import BaseChallenge


class Challenge(BaseChallenge):
    @staticmethod
    def calc_race(times, distances):
        races = zip(times, distances)

        count = 1
        for rt, rd in races:
            max_hold_time = rt // 2
            options = 0
            for v in range(max_hold_time, 0, -1):
                distance = v * (rt - v)
                if distance > rd:
                    options += 2

            if rt % 2 != 1:
                options -= 1

            count *= options

        return count

    def part_1(self):
        time = self.input_lines()[0].split(":")[1]
        distance = self.input_lines()[1].split(":")[1]

        times = ic([int(t.strip()) for t in time.split(" ") if t.strip() != ""])
        distances = ic([int(d.strip()) for d in distance.split(" ") if d.strip() != ""])

        return self.calc_race(times, distances)

    def part_2(self):
        time = self.input_lines()[0].split(":")[1]
        distance = self.input_lines()[1].split(":")[1]

        times = int(time.replace(" ", ""))
        distances = int(distance.replace(" ", ""))

        return self.calc_race((times,), (distances,))


if __name__ == "__main__":
    Challenge().run()
    Challenge(use_test_data=True).run()
