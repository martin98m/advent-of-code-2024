

with open('day-09/input.txt') as f:
    lines = f.read()

    print(len(lines)) 

    file_system = []
    idx = 0
    for i in range(len(lines)):
        
        is_even = i % 2 == 0
        for v in range(int(lines[i])):
            if is_even:
                file_system.append(idx)
            else:
                file_system.append(None)
        
        if is_even:
            idx += 1
    
    new_fs = []
    stack_size = 0
    for i in file_system:
        if i[0]=="F" or i == len(file_system)-1:
            if stack_size>0:
                new_fs.append(("S", stack_size))
                stack_size = 0
            new_fs.append(i)
        else:
            stack_size += i[1]
    file_system = new_fs.copy()
    print(ix)

    total = 0
    for i in range(len(file_system)):
        #print(i, file_system[i])
        total += i*int(file_system[i])
    print(file_system,total, len(file_system))