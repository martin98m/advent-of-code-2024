import re
import math
from egcd import egcd

print(egcd(89, 128))

with open('day-13/input.txt') as fi:

    inputs = fi.read().split("\n\n")
    print(inputs)

    sum = 0
    for input in inputs:
        button_a, button_b, prize = input.splitlines()
        # print(button_a, button_b, prize)

        button_a = list(map(lambda x: int(x), re.findall('\\d+', button_a)))
        button_b = list(map(lambda x: int(x), re.findall('\\d+', button_b)))
        prize = list(map(lambda x: int(x), re.findall('\\d+', prize)))

        print(button_a, button_b, prize)

        # ax + by = c
        # 128x + 89y = 13800
        a = button_a[0] + button_a[1]
        b = button_b[0] + button_b[1]
        c = prize[0] + prize[1]

        print(a, b, c)

        # x = (13800 - 89y)/128
        # 13800 = 89y (mod 128)
        # egcd(128,89) = (1,16,-23)
        e = egcd(a, b)
        print(e)

        # 89y = 13800 (mod 128)
        # Multiplying both sides by the modular inverse -23:
        # y = (-23 * 13800) (mod 128)
        y = (e[2] * c) % a
        # y = 40 (mod 128)

        # x = (c -by)/a
        x = int((c - b*y) / a)
        print(y, x)
        sum += x*3 + y
