

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
    
    
    fs_copy = file_system.copy()
    total = 0
    i = 0
    while True:
        if fs_copy[i] is None:
            new_val = fs_copy.pop()
            while new_val is None:
                new_val = fs_copy.pop()
            if len(fs_copy) < i:
                break
            total += i * new_val
        else:
            total += i * fs_copy[i]
        
        i += 1

        if i >= len(fs_copy):
            break

    total = 0
    for i in range(len(file_system)):
        #print(i, file_system[i])
        total += i*int(file_system[i])
    print(file_system,total, len(file_system))