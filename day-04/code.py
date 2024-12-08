


with open('input.txt') as f:
    lines = f.read().splitlines() 
    
    count = 0
    col, row = len(lines[0]), len(lines)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            # row XMAS
            if x+3 < col: 
                if lines[y][x] == 'X' and lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
                    count += 1
                # row SMAX
                if lines[y][x] == 'S' and lines[y][x+1] == 'A' and lines[y][x+2] == 'M' and lines[y][x+3] == 'X':
                    count += 1

            if y+3 < row:
                # col XMAS
                if lines[y][x] == 'X' and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
                    count += 1
                # col SAMX
                if lines[y][x] == 'S' and lines[y+1][x] == 'A' and lines[y+2][x] == 'M' and lines[y+3][x] == 'X':
                    count += 1
            
            if x+3<col and y+3<col:
                # col XMAS
                if lines[y][x] == 'X' and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
                    count += 1
                 # col SAMX
                if lines[y][x] == 'S' and lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'M' and lines[y+3][x+3] == 'X':
                    count += 1

            if x<col-3 and y<row-3:
                if lines[y][col-x-1] == 'X' and lines[y+1][col-x-2] == 'M' and lines[y+2][col-x-3] == 'A' and lines[y+3][col-x-4] == 'S':
                    count += 1
                 # col SAMX
                if lines[y][col-x-1] == 'S' and lines[y+1][col-x-2] == 'A' and lines[y+2][col-x-3] == 'M' and lines[y+3][col-x-4] == 'X':
                    count += 1
    
    print(count)
    

with open('input.txt') as f:
    lines = f.read().splitlines() 
    
    count = 0
    col, row = len(lines[0]), len(lines)
    for y in range(len(lines)-2):
        for x in range(len(lines[0])-2):

            w1 = lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2]
            w2 = lines[y+2][x] + lines[y+1][x+1] + lines[y][x+2]                   
            
            #print(w1, w2)
            if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM"):
                count +=1
                    

    
    print(count)