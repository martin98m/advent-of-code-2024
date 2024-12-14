

with open('day-09/input.txt') as fi:
    lines = fi.read()

    file_system = []
    idx = 0
    for l in range(len(lines)):
        
        is_even = l % 2 == 0
    
        if is_even:
            file_system.append(("F", int(lines[l]), idx))   
            idx += 1 
        else:
            file_system.append(("S", int(lines[l])))
    
    print(file_system)

    new_fs = []
    for j,v in enumerate(file_system):
        if v[0] == "S":
            new_fs += [None] * v[1]
        else:
            new_fs += [v[2]] * v[1]
    print(new_fs)

    for i in range(idx-1,-1,-1):
        ct = new_fs.count(i)
        space_size = 0
        for j,v in enumerate(new_fs):
            if v == i: break
            if v is not None:
                space_size = 0
                continue
            elif v is None:
                space_size += 1
                
                if space_size == ct:
                    #DELETE+UPDATE

                    for x,y in enumerate(new_fs):
                        if y == i:
                            new_fs[x] = None
                        elif x >= (j-ct+1) and x <=j:
                            new_fs[x] = i
                        else:
                            continue
                    
                    #print("1")
                    break

        print(i)
    print(len(new_fs))
    total = 0
    for i,v in enumerate(new_fs):
        if v is None: continue
        else:
            total += i*v
    print(total)