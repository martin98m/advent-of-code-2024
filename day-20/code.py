from dijkstra import Graph, DijkstraSPF
import copy
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())

def add_edges(map, pos, dist, path, visited):
    i,j = pos
    
    path.append(pos)
    visited.add(pos)
    if map[i][j] == "E":
        print("done", dist)
    top = map[i-1][j]
    bot = map[i+1][j]
    left = map[i][j-1]
    right = map[i][j+1]
    if top != "#" and (i-1,j) not in visited:
        add_edges(map, (i-1,j),dist + 1, path, visited)
    if bot != "#" and (i+1,j) not in visited:
        add_edges(map, (i+1,j),dist + 1, path, visited)
    if left != "#" and (i,j-1) not in visited:
        add_edges(map, (i,j-1),dist + 1, path, visited)
    if right != "#" and (i,j+1) not in visited:
        add_edges(map, (i,j+1),dist + 1, path, visited)



with open('day-20/input.txt') as fi:

    map = fi.read().splitlines()

    h, l = len(map), len(map[0])
    S, E = (73,51), (61,35)
    #S,E = (3,1), (7,5)
    #graph = Graph()
    path = []
    vis = set()
    add_edges(map, S, 0, path, vis)
    
    #graph.add_edge(old_pos, (new_y,new_x), cost)
    #dijkstra = DijkstraSPF(graph, S)
    #dist = dijkstra.get_distance(E)
    
    distances = {}
    for i, pos in enumerate(path):
        distances.update({pos:len(path) - 2 - i})
    #print(dist)

    cheats = {}

    for i in range(1,h-1):
        for j in range(1,l-1):
            val = map[i][j]
            if val != "#": continue

            top = (i-1,j)
            bot = (i+1,j)
            left = (i,j-1)
            right = (i,j+1)
            
            top = distances.get(top)
            bot = distances.get(bot)
            left = distances.get(left)
            right = distances.get(right)
            
            dst = [top,bot,left,right]
            n_max = 0

            for x in range(4):
                for y in range(x+1,4):
                    if dst[x] and dst[y]:
                        res = abs(dst[x] - dst[y])
                        n_max = n_max if res < n_max else res
            n_max = str(n_max - 2)
            #print(new_dist)
            old = cheats.get(n_max)
            if old is None:
                cheats.update({n_max: 1})
            else:
                cheats.update({n_max: old+1})
        print(i)

    
    sum = 0
    for k,v in cheats.items():
        #print(k,v)
        if int(k) > 99:
            sum += v
    print(sum)