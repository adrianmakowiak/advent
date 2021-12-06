class FishSimulation:
    fish_school = []
    days_passed = 0

    def __init__(self, fish_lives):
        for live in fish_lives:
            self.fish_school.append(Fish(live))

    def start(self, days):
        for i in range(days):
            print(i)
            for fish in self.fish_school:
                if fish.day_pass():
                    self.fish_school.append(Fish(9))


class Fish:
    days_to_reproduce = 0

    def __init__(self, days):
        self.days_to_reproduce = int(days)

    def day_pass(self) -> bool:
        if self.days_to_reproduce == 0:
            self.days_to_reproduce = 6
            return True
        self.days_to_reproduce -= 1
        return  False


def main():
    with open('data.txt', 'r') as f:
        fish_school = []
        data = f.readline()
        print(data)
        days_number = 29
        fish_lives = data.strip().split(',')
        fish_sim = FishSimulation(fish_lives)
        fish_sim.start(days_number)
        # print([f.days_to_reproduce for f in fish_sim.fish_school])
        print(len(fish_sim.fish_school))


if __name__ == '__main__':
    main()
