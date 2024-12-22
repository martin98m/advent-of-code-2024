from dijkstra import Graph, DijkstraSPF

with open('day-18/input.txt') as fi:
    rows = [x.split(",") for x in fi.read().splitlines()]

    w,h = 71,71

    map = set()
    for i in range(1024):
        row = rows[i]
        map.add((int(row[1]), (int(row[0]))))

    for x in range(1024,len(rows)):
        
        map.add((int(rows[x][1]), (int(rows[x][0]))))

        graph = Graph()

        for i in range(h):
            for j in range(w):
                new_y, new_x = i - 1, j
                if new_y > -1 and (new_y,new_x) not in map:
                    graph.add_edge((i,j), (new_y,new_x), 1)
                new_y, new_x = i, j -1
                if j - 1 > -1 and (new_y,new_x) not in map: 
                    graph.add_edge((i,j), (new_y,new_x),1)
                new_y, new_x = i, j + 1
                if j + 1 < w and (new_y,new_x) not in map:
                    graph.add_edge((i,j), (new_y,new_x),1)
                new_y, new_x = i + 1, j
                if i + 1 < h and (new_y,new_x) not in map:
                    graph.add_edge((i,j), (new_y,new_x),1)
        
        dijkstra = DijkstraSPF(graph, (0,0))
    
        try:
            res = dijkstra.get_path((h-1,w-1))
            if x == 1024:
                print("P1>",len(res) - 1)
        except:
            print("P2>",x, rows[x])
            exit()
