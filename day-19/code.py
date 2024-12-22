pattern_cache = {}


def find_pattern(pattern, stripes):
    if pattern == '':
        return 1
    elif pattern in pattern_cache:
        return pattern_cache[pattern]
    else:
        matches = 0
        for stripe in stripes:
            if pattern.startswith(stripe):
                new_pattern = pattern[len(stripe):]
                matches += find_pattern(new_pattern, stripes)
        pattern_cache[pattern] = matches
        return matches


with open('day-19/input.txt') as fi:

    stripes, designs = fi.read().split("\n\n")
    stripes = stripes.split(", ")
    designs = designs.split()

    p1, p2 = 0, 0
    for this_pattern in designs:
        res = find_pattern(this_pattern, stripes)
        if res > 0:
            p1 += 1
            p2 += res

    print(p1)
    print(p2)
