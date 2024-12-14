

with open('day-09/input.txt') as fi:
    lines = fi.read()

    file_system = []
    idx = 0
    for si in range(len(lines)):
        
        is_even = si % 2 == 0
        for i in range(int(lines[si])):
            if is_even:
                file_system.append(idx)    
            else:
                file_system.append(None)    

        if is_even:
            idx += 1
    
    for ix in range(idx-1,-1,-1):
        ct = file_system.count(ix)
        #print(ct)
        n_ct = 0
        for i in range(len(file_system)):
            if file_system.index(ix) < i: break
            if file_system[i] is not None:
                n_ct = 0
                continue
            n_ct += 1
            if ct == n_ct:
                for o in range(len(file_system)):
                    if file_system[o] == ix:
                        file_system[o] = None
                file_system = file_system[:i-ct+1] + [ix]*ct +file_system[i+1:]
                break
        #print(1)


    print(file_system)

    line = "00992111777.44.333....5555.6666.....8888"

    sum = 0
    for i in range(len(file_system)):
        if file_system[i] is None: continue
        sum += i*file_system[i]
    print(sum)
    

