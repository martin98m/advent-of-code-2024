import re

space_w = 101  # 11
space_h = 103  # 7


def print_map(arr):

    mapa = ["."*space_w]*space_h

    for i in arr:
        val = mapa[i[1]][i[0]]
        if val == ".":
            val = "1"
        else:
            val = str(int(val)+1)
        mapa[i[1]] = mapa[i[1]][:i[0]] + val + mapa[i[1]][i[0]+1:]
    return mapa


with open('day-14/input.txt') as fi:

    rows = fi.read().splitlines()

    rrows = []
    for row in rows:
        px, py, vx, vy = list(map(lambda x: int(x), re.findall('-?\d+', row)))
        rrows.append((px, py, vx, vy))

    new = []
    for rrow in rrows:
        px, py, vx, vy = px, py, vx, vy = rrow[0], rrow[1], rrow[2], rrow[3]

        px = (px + 100*vx) % space_w
        py = (py + 100*vy) % space_h

        new.append((px, py))

    val = print_map(new)
    q1, q2, q3, q4 = 0, 0, 0, 0
    w_l = int(space_w/2)
    w_r = int(space_h/2)
    for pos in new:
        if pos[0] < w_l and pos[1] < w_r:
            q1 += 1
        elif pos[0] < w_l and pos[1] > w_r:
            q3 += 1
        if pos[0] > w_l and pos[1] < w_r:
            q2 += 1
        if pos[0] > w_l and pos[1] > w_r:
            q4 += 1

    print("P1> " + str(q1*q2*q3*q4))

    i = 0
    f = open("test.txt", "a")

    while i < 10000:
        new.clear()
        for rrow in rrows:
            px, py, vx, vy = rrow[0], rrow[1], rrow[2], rrow[3]
            px = (px + i*vx) % space_w
            py = (py + i*vy) % space_h

            new.append((px, py))
        res = print_map(new)
        f.write(str(i) + "\n")
        for l in res:
            f.write(l + "\n")
        f.write("\n")
        i += 1

    print("p2 done")
