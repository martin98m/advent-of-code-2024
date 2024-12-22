import math

with open('day-20/input.txt') as fi:

    map = fi.read().splitlines()
    h, w = len(map) - 2, len(map[0]) - 2
    S, E = (73, 51), (61, 35)
    # S, E = (3, 1), (7, 5)

    path = []

    pos = S
    last = None
    while True:
        y, x = pos
        val = map[y][x]
        path.append(pos)
        if pos == E:
            break
        for offset_y, offset_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y, new_x = y + offset_y, x + offset_x
            if map[new_y][new_x] != "#" and (new_y, new_x) != last:
                last = pos
                pos = (new_y, new_x)
                break

    distances = {}
    dlzka = len(path) - 1
    for i, pos in enumerate(path):
        distances.update({pos: dlzka - i})

    # P2
    cheats = {}
    visited = set()
    for i, pos in enumerate(path):
        my_pos_dist = distances[pos]
        # distances.pop(pos)
        visited.add(pos)
        for o in range(-20, 21, 1):
            for p in range(-20, 21, 1):
                new_o = pos[0] + o
                new_p = pos[1] + p
                if new_o < 1 or new_o > h:
                    continue
                if new_p < 1 or new_p > w:
                    continue

                next_pos = (new_o, new_p)
                if next_pos not in distances:
                    continue
                if next_pos in visited:
                    continue

                dis = distances[next_pos]

                a = abs(pos[0] - next_pos[0])
                b = abs(pos[1] - next_pos[1])
                hypo = a+b
                if hypo <= 20:
                    diff = abs(dis - my_pos_dist) - (a+b)
                    cheats[diff] = cheats.get(diff, 0) + 1
        print(i)

    sum = 0
    for k, v in cheats.items():
        if k >= 100:
            sum += v
    print("P2>", sum)
