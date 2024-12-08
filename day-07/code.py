import itertools
op1 = "*+"
op2 = "*+|"

def addNums(a, b, op):
    res = str(a)
    if op == "+":
        res = int(a) + int(b)
    elif op == "*":
        res = int(a) * int(b)
    else:
        res = res + b
    return res

with open('day-07/input.txt') as f:
    lines = f.read().splitlines() 
    
    #print(lines)
    
    sum_p1 = 0
    for line in lines:
        res, nums = line.split(":")
        nums = nums.split()
        #print(res, nums)
        
        variations = list(itertools.product(op2, repeat=len(nums)-1))
        #print(variations)
        
        equal = False
        for var in variations:
            sum_nums = nums[0]
            
            for j in range(len(nums)-1):
                op = var[j]
                sum_nums = addNums(sum_nums, nums[j+1], op)

            if(int(sum_nums) == int(res)):
                equal = True
                break
            
        if equal:
            sum_p1 += int(res)
    
    print("P1> ", sum_p1)