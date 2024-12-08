

def check_stuff(nums, second):
    down = True if nums[0]>nums[1] else False
    skip = False
    #print(nums)
    a,b = nums.copy(), nums.copy()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                skip = True
                a.pop(i)
                b.pop(i+1)
                break
            if (nums[i] > nums[i+1]) != down:
                skip = True
                a.pop(i)
                b.pop(i+1)            
                break
            if(abs(nums[i]-nums[i+1]) > 3):
                skip = True
                a.pop(i)
                b.pop(i+1)
                break
    #print(skip, nums, a,b)
    if skip and second:
        return False
    if skip:
        a_res = check_stuff(a, True)
        b_res = check_stuff(b, True)
        return a_res or b_res
    return True


with open('input.txt') as file:
    lines = [line.split() for line in file]
    #print(lines)
    valid = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line))
        res = check_stuff(nums,False)
        print(nums, res)
        if res:
            valid += 1
    print(valid)
        