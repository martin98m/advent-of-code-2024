maxx = 0

def intersection(arrays):
    global maxx
    counts = {}
    for arr in arrays:
        for el in arr:
            counts[el] = counts.get(el,0) + 1
    
    swapped = {}
    for key, value in counts.items():
        swapped.setdefault(value, []).append(key)
    sorted_dict = dict(sorted(swapped.items(), key=lambda item: item[0], reverse=True))

    for key, value in sorted_dict.items():
        if key == len(value) and key > maxx:
            print(",".join(sorted(value)))
            maxx = len(value)

with open('day-23/input.txt') as fi:
    lines = [tuple(line.split("-")) for line in fi.read().splitlines()]

    connections = {}
    for (pc1,pc2) in lines:
        connections[pc1] = connections.get(pc1, []) + [pc2]
        connections[pc2] = connections.get(pc2, []) + [pc1]

    lans = set()
    for key, val in connections.items():
        
        arrs = [val]
        for k in val:
            v = connections[k]
            arrs.append(v + [k])
            res = [value for value in val if value in v]
            for r in res:
                lan = set()
                lan.add(k)
                lan.add(key)
                lan.add(r)
                
                lans.add("".join(sorted(list(lan))))

        intersection(arrs)

    sum = 0
    for l in lans:
        if l[0] == "t" or l[2] == "t" or l[4] == "t":
            sum += 1
    print(sum)
