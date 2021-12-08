init_value = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
}

class FishSimulation:
    fish_school = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    fish_copy = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    def __init__(self, fish_lives):
        for live in fish_lives:
            self.fish_school[int(live)] += 1

    def start(self, days):
        for i in range(days):
            for key, number_fish in self.fish_school.items():
                if key == 0:
                    self.fish_copy[6] += number_fish
                    self.fish_copy[8] += number_fish
                elif key in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    self.fish_copy[key - 1] += number_fish
            self.fish_school = self.fish_copy
            self.fish_copy = init_value.copy()
            print(self.fish_copy)
            # print(f'Days: {i}, fish: {len(self.fish_school)}')
        print(f"fish: {sum(self.fish_school.values())}")


def main():
    with open('data.txt', 'r') as f:
        data = f.readline()
        fish_lives = data.strip().split(',')

        fish_sim = FishSimulation(fish_lives)

        fish_sim.start(256)
        print(fish_sim.fish_school)


if __name__ == '__main__':
    main()
