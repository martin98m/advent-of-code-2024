

with open('input.txt') as file:
    lines = [line.split() for line in file]
    arr1 = list(map(lambda x: int(x[0]), lines))
    arr2 = list(map(lambda x :int(x[1]), lines))
    arr1.sort()
    arr2.sort()
    distance,sim = 0,0
    for i in range(len(arr1)):
        distance += abs(arr1[i] - arr2[i])
        sim += arr1[i] * arr2.count(arr1[i])
    print(distance, sim)