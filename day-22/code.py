

prune = 16777216

with open('day-22/input.txt') as fi:
    changes = {}
    secret_numbers = [int(x) for x in fi.read().splitlines()]
    p1_sum = 0
    for val in secret_numbers:
        sn = val
        change = []
        bananas = []
        prev = sn % 10
        used_patterns = set()
        for j in range(2000):
            # nn = sn * 64
            # sn = nn ^ sn
            # sn = sn % prune
            sn = ((sn * 64) ^ sn) % prune

            # nn = int(sn / 32)
            # sn = nn ^ sn
            # sn = sn % prune
            sn = (int(sn / 32) ^ sn) % prune

            #nn = sn * 2048
            #sn = nn ^ sn
            #sn = sn % prune
            sn = ((sn * 2048) ^ sn ) % prune 

            last_banana = sn % 10
            bananas.append(last_banana)
            change.append(str(last_banana - prev))
            prev = last_banana

            if j > 2:
                bananas = bananas[-4:]
                change = change[-4:]
                key = "".join(change)
                if key in used_patterns:
                    continue
                used_patterns.add(key)
                changes[key] = changes.get(key, 0) + last_banana

        p1_sum += sn
    print(p1_sum)

    p2_key = max(changes, key=changes.get)
    p2_value = changes[p2_key]
    print(p2_value)
