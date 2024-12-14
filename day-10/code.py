
next_map = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9",}

def start_trail(map, y, x, old):
    
    cur = map[y][x]
    if cur == "9":return [(y,x)]
    
    old.add((y,x))
    sum = []

    n = map[y-1][x]
    if next_map[cur] == n and (y-1,x) not in old:
        sum += start_trail(map, y-1, x,old.copy())

    e = map[y][x+1]
    if next_map[cur] == e and (y,x+1) not in old:
        sum += start_trail(map, y, x+1,old.copy())
    
    s = map[y+1][x]
    if next_map[cur] == s and (y+1,x) not in old:
        sum += start_trail(map, y+1, x,old.copy())
    
    w = map[y][x-1]
    if next_map[cur] == w and (y,x-1) not in old:
        sum += start_trail(map, y, x-1,old.copy())

    return sum
    




with open('day-10/input.txt') as file:
    lines = []
    
    lines =[list(line) for line in file.read().splitlines()]
    h,w = len(lines)-2, len(lines[0])-2

    print(h,w)

    p1,p2 = 0,0
    for y in range(1,h+1,1):
        for x in range(1,w+1,1):
            if lines[y][x] == "0":
                old = set()
                res = start_trail(lines, y,x, old)
                p1 += len(set(res))
                p2 += len(res)

    print(p1,p2)