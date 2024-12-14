
def print_fs(arr):
    val=""
    for i, v in enumerate(arr):
        if v[0] == "F":
            for x in range(v[1]):
                val += str(v[2])
        else:
            for x in range(v[1]):
                val += "."
    return val

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

        
    final_fs = file_system.copy()
    for ix in range(idx-1,-1,-1):
        #print(ix)
        file = file_system[ix*2]

        pos = 0
        for i,v in enumerate(final_fs):
            pos += v[1]
            if i > pos: break
            if v[0] == "F":continue
            
            diff = item[1] - found[0][1] 
            if diff < 0:continue
            file_system = file_system[:found[1]] + [("S",found[0][1])] +file_system[found[1]+1:]
            if diff == 0:
                file_system = file_system[:i] + [found[0]] + file_system[i+1:]
            else:
                file_system = file_system[:i] + [found[0]] + [("S", diff)] + file_system[i+1:]
            break

        #new_fs = []
        #stack_size = 0
        #for i in file_system:
        #    if i[0]=="F" or i == len(file_system)-1:
        #        if stack_size>0:
        #            new_fs.append(("S", stack_size))
        #            stack_size = 0
        #        new_fs.append(i)
        #    else:
        #        stack_size += i[1]
        #file_system = new_fs.copy()
        #print(ix)


    #print(file_system)

    line = ""
    sum = 0
    for i in range(len(file_system)):
        item = file_system[i]
        if item[0] == "S":
            for j in range(item[1]):
                 line += "."
        else:
            for j in range(item[1]):
                 line += str(item[2])
    
    sum = 0
    for i in range(len(line)):
        item = line[i]
        if item == ".":continue
        sum += i * int(line[i])
    print(sum)
    

