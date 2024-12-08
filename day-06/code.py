import time

start = time.time()
print("hello")

movement_map = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1)}
rotation_map = {"N":"E","E":"S","S":"W","W":"N"}


with open('input.txt') as f:
    lines = f.read().splitlines() 
    
    #pos = (6,4,"N")
    pos = (60,60,"N")
    
    p1_set, p2_set = set(), set()
    p1_set.add((pos[0],pos[1]))
    p2_set.add(pos)
    
    #wall = 9
    wall = 129
    
    move = True
    while move:
        movement = movement_map[pos[2]]
        
        next_location = (pos[0]+movement[0], pos[1]+movement[1], pos[2])
        
        if(next_location[0] < 0 or next_location[1] < 0 or next_location[0]>wall or next_location[1]>wall):
            move = False
            break
        next_location_value = lines[next_location[0]][next_location[1]]

        if next_location_value == "#":
            pos = (pos[0],pos[1],rotation_map[pos[2]])
        else:
            pos = (next_location[0], next_location[1],pos[2])
        p1_set.add((pos[0],pos[1]))
        if pos in p2_set:
            print("infinity")
            move = False
    print("Finished", len(p1_set))
    end = time.time()
    print(end - start)
    inf = 0
    for i in range(wall+1):
        for j in range(wall+1):
            val = lines[i][j]
            
            if val == "#" or val == "^":
                continue
                
            new_map = lines.copy()
            new_map[i] = new_map[i][:j] + "#" + new_map[i][j+1:]
            #print(new_map)
            p2_set.clear()
            #pos = (6,4,"N")
            pos = (60,60,"N")

            move = True
            while move:
                movement = movement_map[pos[2]]
                
                next_location = (pos[0]+movement[0], pos[1]+movement[1], pos[2])
                
                if(next_location[0] < 0 or next_location[1] < 0 or next_location[0]>wall or next_location[1]>wall):
                    move = False
                    break
                next_location_value = new_map[next_location[0]][next_location[1]]

                if next_location_value == "#":
                    pos = (pos[0],pos[1],rotation_map[pos[2]])
                else:
                    pos = (next_location[0], next_location[1],pos[2])
                if pos in p2_set:
                    #print("infinity")
                    inf += 1
                    move = False
                p2_set.add(pos)
    print("Finished", inf)
    end = time.time()
    print(end - start)
            