import re

with open('day-13/input.txt') as fi:

    inputs = fi.read().split("\n\n")

    sum = 0
    for input in inputs:
        button_a, button_b, prize = input.splitlines()

        button_a = list(map(lambda x: int(x), re.findall('\\d+', button_a)))
        button_b = list(map(lambda x: int(x), re.findall('\\d+', button_b)))
        prize = list(map(lambda x: int(x) + 10000000000000, re.findall('\\d+', prize)))

        # [92 22] [X]   [8400]
        # [34 67] [Y]   [5400]
        det = button_a[0] * button_b[1] - button_a[1] * button_b[0]
        if det == 0:
            continue
        #[8400 22]
        #[5400 67]
        A = (prize[0]*button_b[1] - prize[1]*button_b[0]) / det
        
        #[92 8400]
        #[34 5400]
        B = (button_a[0]*prize[1] - button_a[1] * prize[0]) / det

        if A.is_integer() and B.is_integer():
            sum += int(A) * 3 + int(B)
    
    print(sum)

