import heapq
from collections import deque


def find_position(grid, char):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == char:
                return (x, y)


def a_star(grid, start, end, initial_direction):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    directions = {
        (0, 1): "down",
        (1, 0): "right",
        (0, -1): "up",
        (-1, 0): "left"
    }

    open_set = []
    heapq.heappush(open_set, (0, start, initial_direction))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current, prev_dir = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, g_score[end]

        for (dx, dy), direction in directions.items():
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor

            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#':
                turn_cost = 1000 if prev_dir and prev_dir != direction else 0
                tentative_g_score = g_score[current] + 1 + turn_cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + \
                        heuristic(neighbor, end)
                    heapq.heappush(
                        open_set, (f_score[neighbor], neighbor, direction))

    return None, float('inf')


touched = set()


def a_star_p2(grid, start, end, initial_direction, limit):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    directions = {
        (0, 1): "down",
        (1, 0): "right",
        (0, -1): "up",
        (-1, 0): "left"
    }

    open_set = []
    came_from = set()
    heapq.heappush(open_set, (0, (start, initial_direction), came_from))

    g_score = {(start, initial_direction): 0}
    f_score = {(start, initial_direction): heuristic(start, end)}

    while open_set:
        _, (current, prev_dir), visited = heapq.heappop(open_set)
        new_visited = visited.copy()
        new_visited.add(current)
        if current == end:
            # print("Reached end")
            # for ooo in range(len(grid)):
            #    to_print = ""
            #    for ppp in range(len(grid[0])):
            #        val =grid[ooo][ppp]
            #        if (ppp,ooo) in visited:
            #            val = "O"
            #        to_print += val
            #    print(to_print)
            for current in visited:
                touched.add(current)
            continue

        for (dx, dy), direction in directions.items():
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor

            if neighbor in visited:
                continue

            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#':

                turn_cost = 1000 if prev_dir and prev_dir != direction else 0
                tentative_g_score = g_score[(
                    current, prev_dir)] + 1 + turn_cost
                if tentative_g_score > limit:
                    continue

                if (neighbor, direction) not in g_score or tentative_g_score < g_score[(neighbor, direction)]:
                    g_score[(neighbor, direction)] = tentative_g_score
                    f_score[(neighbor, direction)] = tentative_g_score + \
                        heuristic(neighbor, end)
                    heapq.heappush(
                        open_set, (f_score[(neighbor, direction)], (neighbor, direction), new_visited))
                elif tentative_g_score == g_score[(neighbor, direction)]:
                    heapq.heappush(
                        open_set, (f_score[(neighbor, direction)], (neighbor, direction), new_visited))

    return None, float('inf')


with open('day-16/input.txt') as fi:

    grid = fi.read().splitlines()

    start = find_position(grid, 'S')
    end = find_position(grid, 'E')

    path, cost = a_star(grid, start, end, "right")
    print(cost)

    path_p2 = a_star_p2(grid, start, end, "right", cost)
    print(len(touched) + 1)
