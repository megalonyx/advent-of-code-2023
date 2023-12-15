#!/usr/bin/env python3

# format: (row, column) as deltas
NORTH = (-1, 0)
SOUTH = (1, 0)
WEST  = (0, -1)
EAST  = (0, 1)

NEIGHBOURS = {
'|': [NORTH, SOUTH],
'-': [WEST, EAST],
'L': [NORTH, EAST],
'J': [NORTH, WEST],
'7': [SOUTH, WEST],
'F': [SOUTH, EAST],
'.': [],
'S': []   # needs to be determined based on map
}

looppart = []

def read_map(filename):
    global looppart
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            cols = [ c for c in line.strip() ]
            rows.append(cols)
            looppart.append( [ False for _ in range(len(cols)) ] )
    return rows

def find_start(rows):
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            if rows[r][c] == 'S':
                return (r, c)
    return None

def replace_start(rows, pos):
    r, c = pos
    # four adjacent positions:
    north = rows[r-1][c]
    connected_north = (north == '|' or north == '7' or north == 'F')
    south = rows[r+1][c]
    connected_south = (south == '|' or south == 'L' or south == 'J')
    west = rows[r][c-1]
    connected_west = (west == '-' or west == 'L' or west == 'F')
    east = rows[r][c+1]
    connected_east = (east == '-' or east == 'J' or east == '7')
    if connected_north and connected_west:
        rows[r][c] = 'J'
    elif connected_north and connected_south:
        rows[r][c] = '|'
    elif connected_north and connected_east:
        rows[r][c] = 'L'
    elif connected_south and connected_west:
        rows[r][c] = '7'
    elif connected_south and connected_east:
        rows[r][c] = 'F'
    elif connected_west and connected_east:
        rows[r][c] = '-'
    else:
        print('error')
        exit(-1)
    
def start_advancing(rows, start):
    global looppart
    distance = 0
    current = start
    # choose one direction:
    (r, c) = current
    ici = rows[r][c]
    neighbours = NEIGHBOURS[ici]
    from_direction = (-neighbours[0][0], -neighbours[0][1])
    while True:
        looppart[current[0]][current[1]] = True
        print(current, from_direction)
        distance += 1
        nextdir = advance(rows, current, from_direction)
        current = ( current[0] + nextdir[0], current[1] + nextdir[1] )
        from_direction = nextdir
        if current == start:
            return distance

# we are at 'here', we arrived at 'here' by choosing direction 'coming_from_direction' of
# the former position
def advance(rows, here, coming_from_direction):
    (r, c) = here
    pipepiece = rows[r][c]
    neighbours = NEIGHBOURS[pipepiece]
    print('at', here, 'neighbours:', neighbours)
    inverted_direction = (-coming_from_direction[0],-coming_from_direction[1])
    if neighbours[0] == inverted_direction:
        new_direction = neighbours[1]
    elif neighbours[1] == inverted_direction:
        new_direction = neighbours[0]
    else:
        print('direction mismatch')
        exit(-1)
    print('choosing dir:', new_direction)
    return new_direction
    
def count_field(rows, r, c):
    nrows = len(rows)
    ncols = len(rows[0])
    if looppart[r][c]:
        return 0
    crossings = 0
    r2, c2 = r, c
    while r2 < nrows and c2 < ncols:
        x = rows[r2][c2]
        if looppart[r2][c2] and x != 'L' and x != '7':
            crossings += 1
        r2 += 1
        c2 += 1
    return crossings % 2

def count_inside(rows):
    total = 0
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            total += count_field(rows, r, c)
    return total

def main():
#    rows = read_map('test1.txt')
#    rows = read_map('test2.txt')
#    rows = read_map('test3.txt')
    rows = read_map('input.txt')
    start = find_start(rows)
    replace_start(rows, start)
    dist = start_advancing(rows, start)
    print(count_inside(rows))

if __name__ == '__main__':
    main()
