
with open('input.txt') as f:
    lines = f.read().split("\n\n") 
    maps = lines[0].splitlines()
    paths = lines[1].splitlines()
    
    unique_nums= set()
    l,r = [],[]
    for x in maps:
        key, val = x.split("|")
        unique_nums.add(key)
        unique_nums.add(val)
        l.append(key)
        r.append(val)
    
    sumOk = 0
    sumNok = 0

    for row in paths:
        pos = 0
        ok = True
        arr = row.split(",")
        arr2 = arr.copy()
        
        order = []
        new_l, new_r = [],[]
        for i in range(len(r)):
            if r[i] in arr and l[i] in arr:
                new_l.append(l[i])
                new_r.append(r[i])
        print(new_l, new_r)
        while len(arr2)>0:
            print(list(map(lambda x: new_r.count(x), arr2)))
            i = list(filter(lambda x: new_r.count(x) == 0, arr2))[0]
            #print(i)
            order.append(i)
            arr2.remove(i)
            for o in range(new_l.count(i)):
                ind = new_l.index(i)
                new_l = new_l[:ind]+new_l[ind+1:]
                new_r = new_r[:ind]+new_r[ind+1:]
        print(order)
        
        
        for num in arr:
            new_pos = order.index(num)
            #print(new_pos)
            if new_pos < pos:
                ok = False
                break
            pos = new_pos
        print(row, ok)
        pos = int(len(arr)/2)
        if ok:
            sumOk += int(arr[pos])
        else:
            sumNok += int(order[pos])
            
        
    print(sumOk, sumNok)
    