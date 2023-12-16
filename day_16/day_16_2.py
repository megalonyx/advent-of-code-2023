#!/usr/bin/env python3

#import numpy as np

# a beam has a position (r, c) and a direction (dr, dc)

def read_rows(filename):
    rows = []
    with open(filename, 'r') as f:
        while line := f.readline():
            line = line.strip()
            rows.append(line)
    return rows

# returns beam if beam continues, None if beam moved outside
def advance_beam(rows, energized, beams, visited, thisbeam):
    numrows = len(rows)
    numcols = len(rows[0])
    pos, direc = thisbeam
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
        thisbeam = ((newr, newc), (dr, dc))
    elif ici == '/':
        newdr = -dc
        newdc = -dr
        thisbeam = ((newr, newc), (newdr, newdc))
    elif ici == '\\':
        newdr = dc
        newdc = dr
        thisbeam = ((newr, newc), (newdr, newdc))
    elif ici == '-':
        if dc != 0:
            thisbeam = ((newr, newc), (dr, dc))
        else:
            beam1 = ((newr, newc), (0, -1))
            beam2 = ((newr, newc), (0, 1))
            thisbeam = beam1
            beams.append(beam2)
    elif ici == '|':
        if dr != 0:
            thisbeam = ((newr, newc), (dr, dc))
        else:
            beam1 = ((newr, newc), (-1, 0))
            beam2 = ((newr, newc), (1, 0))
            thisbeam = beam1
            beams.append(beam2)
    else:
        print('unknown:', ici)
        exit(-1)
    return thisbeam

def count_energized(energized):
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

def energized_for_entering_beam(rows, thisbeam):
    energized = []
    for r in range(len(rows)):
        row = []
        for c in range(len(rows[0])):
            row.append('.')
        energized.append(row)
    beams = [thisbeam]
    visited = set()
    while len(beams) > 0:
        beam = beams.pop()
        while beam:
            beam = advance_beam(rows, energized, beams, visited, beam)
    return count_energized(energized)

def main():
#    rows = read_rows('test.txt')
    rows = read_rows('input.txt')
    maxene = 0
    # from the left:
    for r in range(len(rows)):
        beam = ((r, -1), (0, 1))
        ene = energized_for_entering_beam(rows, beam)
        maxene = max(maxene, ene)
        print(r, ene)
    # from the right:
    for r in range(len(rows)):
        beam = ((r, len(rows[0])), (0, -1))
        ene = energized_for_entering_beam(rows, beam)
        maxene = max(maxene, ene)
        print(r, ene)
    # from the top:
    for c in range(len(rows[0])):
        beam = ((-1, c), (1, 0))
        ene = energized_for_entering_beam(rows, beam)
        maxene = max(maxene, ene)
        print(r, ene)
    # from the bottom:
    for c in range(len(rows[0])):
        beam = ((len(rows), c), (-1, 0))
        ene = energized_for_entering_beam(rows, beam)
        maxene = max(maxene, ene)
        print(r, ene)

    print('max:', maxene)


if __name__ == '__main__':
    main()
