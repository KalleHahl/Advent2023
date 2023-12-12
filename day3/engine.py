engine = []

with open('engine.txt', 'r') as file:
    for line in file:
        engine.append(list(line.strip()))
    
def engine_parts(engine):
    parts = 0
    num = ''
    for row_i,row in enumerate(engine):
        for col_i,col in enumerate(row):
            if col.isdigit():
                num += col
                if col_i != len(row)-1:
                    continue
        
            if not num:
                continue
            col_start = col_i-1-len(num) if col_i-len(num) != 0 else col_i-len(num)
            if col_i == len(row)-1 and col.isdigit():
                col_start = col_i-len(num)
            col_end = col_i+1
            row_start = row_i-1 if row_i != 0 else 0
            row_end = row_i+2 if row_i != len(engine)-1 else row_i+1
            found = False
            for a in range(row_start,row_end):
                for b in range(col_start, col_end):
                    if not engine[a][b].isdigit() and engine[a][b] != '.':
                        if not found:
                            parts += int(num)
                            found = True
            num = ''

    return parts

def gears(engine):
    parts = 0
    for row_i,row in enumerate(engine):
        for col_i,col in enumerate(row):
            if col == '*':
                row_start = row_i-1 if row_i != 0 else 0
                row_end = row_i+2 if row_i != len(engine)-1 else row_i+1
                col_start = col_i-1 if col_i != 0 else 0
                col_end = col_i+2 if col_i != len(row)-1 else col_i+1
                parts_near = set()
                for a in range(row_start,row_end):
                    for b in range(col_start, col_end):
                        if engine[a][b].isdigit():
                            left = b
                            left_side= ''
                            while left-1>=0:
                                left -= 1
                                if engine[a][left].isdigit():
                                    left_side+=engine[a][left]
                                    continue
                                break
                            right = b
                            right_side = engine[a][b]
                            while right+1<len(row):
                                right += 1
                                if engine[a][right].isdigit():
                                    right_side+=engine[a][right]
                                    continue
                                break
                            parts_near.add(int(left_side[::-1]+right_side))
                if len(parts_near) == 2:
                    parts_list = list(parts_near)
                    parts += parts_list[0]*parts_list[1]
    return parts
                                
                                

    
                

print(engine_parts(engine))
print(gears(engine))


