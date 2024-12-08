import re

with open('input.txt') as file:
    total = 0
    for line in file.readlines(): 
    
        regex = "mul\\(\\d{1,3},\\d{1,3}\\)"
        res = re.findall(regex, line)
        #print(len(res))
        
        for f in res:
            nums = re.search("(\\d+),(\\d+)",f)
            mul = nums.group().split(",")
            total += int(mul[0]) * int(mul[1])
    print(total)

with open('input.txt') as file:
    total = 0
    do = True

    for line in file.readlines(): 
    
        regex = "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)"
        res = re.findall(regex, line)
        #print(len(res))
        for f in res:
            if f == "do()":
                do = True
            elif f == "don't()":
                do = False
            else:
                if not do:
                    continue
                nums = re.search("(\\d+),(\\d+)",f)
                mul = nums.group().split(",")
                total += int(mul[0]) * int(mul[1])
    print(total)