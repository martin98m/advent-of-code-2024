from dijkstra import Graph, DijkstraSPF
import sys
import copy

print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

paths = {(0, 1): [(-1, 0), (0, 1), (1, 0)], (-1, 0): [(0, -1), (-1, 0), (0, 1)],
             (0, -1): [(1, 0), (0, -1), (-1, 0)], (1, 0): [(0, 1), (1, 0), (0, -1)]}

min = 100000
S, E = (139, 1), (1, 139)

def explore(old_pos, facing, visited, graph, total_cost):
    global paths, min, S, E

    visited.add(old_pos)
    for i, dir in enumerate(paths[facing]):
        new_y, new_x = old_pos[0] + dir[0], old_pos[1] + dir[1]
        
        if (new_y,new_x) in visited: continue
        
        cur = map_inp[new_y][new_x]
        if cur == "#": continue

        cost = 1 if i == 1 else 1001
        if total_cost + cost > min: continue

        graph.add_edge(old_pos, (new_y,new_x), cost)
        if cur == "E":
            dijkstra = DijkstraSPF(graph, S)
            dist = dijkstra.get_distance(E)
            if dist < min:
                min = dist
            print(dist)
            continue

        explore((new_y, new_x), dir, visited.copy(), copy.deepcopy(graph), total_cost+cost)


with open('day-16/input.txt') as fi:

    map_inp = fi.read().splitlines()

    h, w = len(map_inp), len(map_inp[0])

    facing = (0, 1)

    graph = Graph()

    explore(S,facing,set(),graph,0)

    print(min)



    # cur = map_inp[i][j]
    # if cur == "#":continue
    # elif cur == "S":
    #    S = (i,j)
    # elif cur == "E":
    #    S = (i,j)
