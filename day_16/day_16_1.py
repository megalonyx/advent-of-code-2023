#!/usr/bin/env python3

#import numpy as np

# a beam has a position (r, c) and a direction (dr, dc)

energized = []
beams = []
visited = set()

def read_rows(filename):
    global energized
    rows = []
    with open(filename, 'r') as f:
        while line := f.readline():
            line = line.strip()
            rows.append(line)
            energized.append((['.' for c in line]))
    return rows

# returns beam if beam continues, None if beam moved outside
def advance_beam(rows, beam):
    global beams
    numrows = len(rows)
    numcols = len(rows[0])
    pos, direc = beam
    r, c = pos
    dr, dc = direc
    newr = r + dr
    newc = c + dc
    if newr < 0 or newr >= numrows:
        return None
    if newc < 0 or newc >= numcols:
        return None
    energized[newr][newc] = '#'
    if ((r,c),(dr,dc)) in visited:
        return None
    else:
        visited.add( ((r,c),(dr,dc)) )
    ici = rows[newr][newc]
    if ici == '.':
        beam = ((newr, newc), (dr, dc))
    elif ici == '/':
        newdr = -dc
        newdc = -dr
        beam = ((newr, newc), (newdr, newdc))
    elif ici == '\\':
        newdr = dc
        newdc = dr
        beam = ((newr, newc), (newdr, newdc))
    elif ici == '-':
        if dc != 0:
            beam = ((newr, newc), (dr, dc))
        else:
            beam1 = ((newr, newc), (0, -1))
            beam2 = ((newr, newc), (0, 1))
            beam = beam1
            beams.append(beam2)
    elif ici == '|':
        if dr != 0:
            beam = ((newr, newc), (dr, dc))
        else:
            beam1 = ((newr, newc), (-1, 0))
            beam2 = ((newr, newc), (1, 0))
            beam = beam1
            beams.append(beam2)
    else:
        print('unknown:', ici)
        exit(-1)
    return beam

def count_energized():
    total = 0
    for r in range(len(energized)):
        for c in range(len(energized[0])):
            total += 1 if energized[r][c] == '#' else 0
    return total

def print_rows(rows):
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            print(rows[r][c], end='')
        print()
    print()

def main():
    global beams
    rows = read_rows('test.txt')
#    rows = read_rows('input.txt')
    beam = ((0, -1), (0, 1))
    beams.append(beam)
    while len(beams) > 0:
        beam = beams.pop()
        while beam:
            beam = advance_beam(rows, beam)
            #print(beam)
    print_rows(rows)
    print_rows(energized)
    print(count_energized())


if __name__ == '__main__':
    main()
