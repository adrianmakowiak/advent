from collections import Counter
def main():
    nodes = {}

    with open('data.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            a, b = line.strip().split('-')
            if b != 'start' and a != 'end':
                if a in nodes:
                    nodes[a].append(b)
                else:
                    nodes[a] = [b]

            if a != 'start' and b != 'end':
                if b in nodes:
                    nodes[b].append(a)
                else:
                    nodes[b] = [a]

        check_tree(nodes)


PATHS = []


def check_sub_tree(nodes, current_node, so_far):
    if current_node == 'end':
            print(f'Congrats, you found:{so_far}')
            PATHS.append(so_far)
            return
    for n in nodes[current_node]:
        counted = Counter(so_far)
        already_has_two_small = False
        for cave, occurrences in counted.items():
            if cave.islower() and occurrences > 1:
                already_has_two_small = True
        if n.islower() and n in counted and (counted[n] > 1 or (counted[n] == 1 and already_has_two_small)):
            continue

        new_path = [*so_far, n]
        check_sub_tree(nodes, n, new_path)


def check_tree(nodes):
    start_nodes = nodes['start']
    for n in start_nodes:
        new_path = [n]
        check_sub_tree(nodes, n, new_path)

    print(len(PATHS))


if __name__ == '__main__':
    main()
