import numpy as np
class FishSimulation:
    fish_school = []
    days_passed = 0

    def __init__(self, fish_lives):
        for live in fish_lives:
            self.fish_school.append(Fish(live))

    def start(self, days):
        for i in range(days):
            for fish in self.fish_school:
                if fish.day_pass():
                    self.fish_school.append(Fish(9))
            # print(f'Day: {i+1} {[f.days_to_reproduce for f in self.fish_school]}')
            print(f'Days: {i}, fish: {len(self.fish_school)}')
        print(f"fish: {len(self.fish_school)}")


class Fish:
    days_to_reproduce = 0

    def __init__(self, days):
        self.days_to_reproduce = int(days)

    def day_pass(self) -> bool:
        if self.days_to_reproduce == 0:
            self.days_to_reproduce = 6
            return True
        self.days_to_reproduce -= 1
        return False


def main():
    with open('data.txt', 'r') as f:
        data = f.readline()
        fish_lives = data.strip().split(',')
        rates = []
        fish_sim = FishSimulation([6])
        for i in range(100):
            fish_sim.start(1)
            rates.append(len(fish_sim.fish_school))
            # print(f'## {len(fish_sim.fish_school)}')

        growth_rate = np.exp(np.diff(np.log(rates))) - 1
        print(growth_rate)
        print(np.average(growth_rate))
if __name__ == '__main__':
    main()
