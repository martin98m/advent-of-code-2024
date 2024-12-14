from functools import cache


@cache
def rules(stone, blink):

    if blink == 0:
        return 1

    l = len(stone)

    if stone == "0":
        return rules("1", blink - 1)
    elif l % 2 == 0:
        return rules(stone[:l//2], blink - 1) + rules(str(int(stone[l//2:])), blink - 1)
    else:
        return rules(str(int(stone)*2024), blink - 1)


with open('day-11/input.txt') as fi:

    stones = fi.read().split()

    print(sum(rules(stone, 25) for stone in stones))
    print(sum(rules(stone, 75) for stone in stones))
