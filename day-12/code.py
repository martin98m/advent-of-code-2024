explored_plots = set()


def explore_garden(garden, pos):

    if pos in explored_plots:
        return None
    explored_plots.add(pos)

    y, x = pos
    plant = garden[y][x]

    neighbours = [(y-1, x), (y+1, x), (y, x-1), (y, x+1),
                  (y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]

    neigh_vals = []
    cardinal_neigh = []
    area, perimeter, edges = 1, 0, 0
    for i, neigh in enumerate(neighbours):
        new_y, new_x = neigh

        if new_y < 0 or new_y > len(garden) - 1:
            neigh_vals.append(None)
            continue
        if new_x < 0 or new_x > len(garden[0]) - 1:
            neigh_vals.append(None)
            continue

        n_v = garden[new_y][new_x]
        neigh_vals.append(n_v)

        if i > 3:
            continue

        cardinal_neigh.append(n_v)
        if neigh in explored_plots:
            continue
        if n_v != plant:
            continue
        a, p, e = explore_garden(garden, (new_y, new_x))
        area += a
        perimeter += p
        edges += e

    c_l = len(cardinal_neigh)
    fence = 4 - c_l + c_l - cardinal_neigh.count(plant)
    perimeter += fence

    _t, _b, _l, _r, _tl, _tr, _bl, _br = neigh_vals
    if _t != plant and _l != plant:
        edges += 1
    if _t != plant and _r != plant:
        edges += 1
    if _b != plant and _l != plant:
        edges += 1
    if _b != plant and _r != plant:
        edges += 1

    if _t == plant and _l == plant and _tl != plant:
        edges += 1
    if _t == plant and _r == plant and _tr != plant:
        edges += 1
    if _b == plant and _l == plant and _bl != plant:
        edges += 1
    if _b == plant and _r == plant and _br != plant:
        edges += 1

    return area, perimeter, edges


with open('day-12/input.txt') as fi:
    garden = [[x for x in row] for row in fi.read().splitlines()]

    p1, p2 = 0, 0
    for y in range(len(garden)):
        for x in range(len(garden[0])):
            res = explore_garden(garden, (y, x))
            if res:
                p1 += res[0] * res[1]
                p2 += res[0] * res[2]

    print(p1)
    print(p2)
