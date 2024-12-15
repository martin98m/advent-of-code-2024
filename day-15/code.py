map_p1 = []
map_p2 = []
robot_pos = (4, 8)  # (3,10)#(24,24)
dir_map = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}


def move_p1(pos, dir, char):
    global robot_pos
    vec = dir_map[dir]

    y = pos[0] + vec[0]
    x = pos[1] + vec[1]

    val = map_p1[y][x]

    if val == "#":
        return False
    elif val == ".":
        map_p1[y][x] = char
        map_p1[pos[0]][pos[1]] = "."
        if char == "@":
            robot_pos = (y, x)
        return True
    else:
        res = move_p1((y, x), dir, val)
        if res:
            map_p1[y][x] = char
            map_p1[pos[0]][pos[1]] = "."
            if char == "@":
                robot_pos = (y, x)
        return res


def explore_p2(pos, dir):
    vec = dir_map[dir]

    y = pos[0] + vec[0]
    x = pos[1] + vec[1]

    val = map_p2[y][x]

    if val == "#":
        return False
    elif val == ".":
        return True
    elif val == "[":
        l1 = explore_p2((y, x), dir)
        l2 = True
        if dir != "<":
            l2 = explore_p2((y, x+1), dir)
        return l1 and l2
    elif val == "]":
        l1 = explore_p2((y, x), dir)
        l2 = True
        if dir != ">":
            l2 = explore_p2((y, x-1), dir)
        return l1 and l2


def move_p2(pos, dir, char, move):

    if not move:
        move_posible = explore_p2(pos, dir)

        if not move_posible:
            return

    global robot_pos
    vec = dir_map[dir]

    y = pos[0] + vec[0]
    x = pos[1] + vec[1]

    val = map_p2[y][x]

    if val == "#":
        return
    elif val == ".":
        map_p2[y][x] = char
        map_p2[pos[0]][pos[1]] = "."
    elif val == "[":
        move_p2((y, x), dir, val, True)
        map_p2[y][x] = char
        map_p2[pos[0]][pos[1]] = "."
        # map_p2[pos[0]][pos[1]] = "."
        if dir == "^" or dir == "v":
            move_p2((y, x+1), dir, "]", True)
    elif val == "]":
        move_p2((y, x), dir, val, True)
        map_p2[y][x] = char
        map_p2[pos[0]][pos[1]] = "."
        # map_p2[pos[0]][pos[1]] = "."

        if dir == "^" or dir == "v":
            move_p2((y, x-1), dir, "[", True)

    if char == "@":
        map_p2[pos[0]][pos[1]] = "."
        robot_pos = (y, x)


with open('day-15/input.txt') as fi:

    map_inp, movements = fi.read().split("\n\n")

    for line in map_inp.splitlines():
        row_p1 = []
        row_p2 = []
        for col in line:
            row_p1.append(col)
            if col == "#":
                row_p2.append(col)
                row_p2.append(col)
            elif col == ".":
                row_p2.append(col)
                row_p2.append(col)
            elif col == "O":
                row_p2.append("[")
                row_p2.append("]")
            else:
                row_p2.append(col)
                row_p2.append(".")
        map_p1.append(row_p1)
        map_p2.append(row_p2)

    for dir in movements:
        if dir == "\n":
            continue
        # move_p1(robot_pos,dir,"@")
        move_p2(robot_pos, dir, "@", False)
        print(dir)

    gps_p1 = 0
    for i in range(len(map_p1)):
        for j in range(len(map_p1[0])):
            if map_p1[i][j] == "O":
                gps_p1 += 100 * i + j
    gps_p2 = 0
    for i in range(len(map_p2)):
        for j in range(len(map_p2[0])):
            if map_p2[i][j] == "[":
                gps_p2 += 100 * i + j

    print(gps_p1, gps_p2)
#
