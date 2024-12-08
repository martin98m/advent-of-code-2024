import time

start = time.time()

with open('day-08/input.txt') as f:
    lines = f.read().splitlines() 
    
    #print(len(lines), len(lines[0]))
    #filled= set()
    dict = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            val = lines[i][j] 
            if ( val == "."):
                continue
            
            #filled.add((i,j))
            if val in dict:
                arr = dict[val]
                arr.append((i,j))
            else:
                dict[val] = [(i,j)]
            #print(i, j, lines[i][j])
            #    if
    
    #print(dict)
    final_pos = set()
    for key in dict:
       

        for pos in range(len(dict[key])):
            for i in range(len(dict[key])-pos-1):
                new_p1 = dict[key][pos]
                new_p2 = dict[key][pos+i+1]  
                #print(new_p1, new_p2)
                
                diff_y = abs(new_p1[0] - new_p2[0])
                diff_x = new_p1[1] - new_p2[1]
                #print( diff_y, diff_x)
                #anti = [(new_p1[0] - diff_y, new_p1[1]),(new_p2[0] - diff_y, )] 
                anti = []
                #if diff_x > 0:
                #    new_p1 = (new_p1[0] - diff_y, new_p1[1]+diff_x)
                #    new_p2 = (new_p2[0] + diff_y, new_p2[1]-diff_x)
                #else:
                #    new_p1 = (new_p1[0] - diff_y, new_p1[1]+diff_x)
                #    new_p2 = (new_p2[0] + diff_y, new_p2[1]-diff_x)
                ##print(anti)
                #anti.append(new_p1)
                #anti.append(new_p2)
                
                for i in range(1000):
                    if diff_x > 0:
                        new_p1 = (new_p1[0] - diff_y, new_p1[1]+diff_x)
                        new_p2 = (new_p2[0] + diff_y, new_p2[1]-diff_x)
                    else:
                        new_p1 = (new_p1[0] - diff_y, new_p1[1]+diff_x)
                        new_p2 = (new_p2[0] + diff_y, new_p2[1]-diff_x)
                    anti.append(new_p1)
                    anti.append(new_p2)
                    
                for x in anti:
                    if x[0]<0:continue
                    if x[1]<0:continue
                    if x[0]>=len(lines):continue
                    if x[1]>=len(lines[0]):continue
                    
                    #if(x in filled):continue
                    final_pos.add(x)
        #print("#")
    #print(len(final_pos), final_pos)
    
    for x in final_pos:
        row = lines[x[0]]
        lines[x[0]] = row[:x[1]] + "#" + row[x[1]+1:]
        
    c = 0
    for line in lines:
        c += line.count(".")
    
    print(len(lines) * len(lines[0]) - c)
        
    print( time.time() - start)
    #print(1)
    #res = list(filter(lambda x: not(x in filled) and x[0]>0 and x[0]<len(lines) and x[1]>0 and x[1]<len(lines[0]),final_pos))
    #print(len(res), res)