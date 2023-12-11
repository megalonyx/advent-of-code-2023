#!/usr/bin/env python3

EXPANSION_DISTANCE = 1000000-1

def read_map(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            cols = line.strip()
            rows.append(cols)
    return rows

def find_galaxies(rows):
    galaxies = []
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == '#':
                galaxies.append( (r, c) )
    return galaxies

def is_row_empty(rows, r):
    for c in rows[r]:
        if c != '.':
            return False
    return True

def is_column_empty(rows, c):
    for r in range(len(rows)):
        if rows[r][c] != '.':
            return False
    return True

def expand_space(rows, galaxies):
    empty_rows = []
    for r in range(len(rows)):
        if is_row_empty(rows, r):
            empty_rows.append(r)
    empty_columns = []
    for c in range(len(rows[0])):
        if is_column_empty(rows, c):
            empty_columns.append(c)
    # expand row and col numbers:
    for i in range(len(empty_rows)):
        empty_rows[i] += i * EXPANSION_DISTANCE
    for i in range(len(empty_columns)):
        empty_columns[i] += i * EXPANSION_DISTANCE
    # expand galaxies by row:
    for er in empty_rows:
        for i in range(len(galaxies)):
            gal = galaxies[i]
            if gal[0] > er:
                galaxies[i] = (gal[0] + EXPANSION_DISTANCE, gal[1])
    # expand galaxies by column:
    for ec in empty_columns:
        for i in range(len(galaxies)):
            gal = galaxies[i]
            if gal[1] > ec:
                galaxies[i] = (gal[0], gal[1] + EXPANSION_DISTANCE)

def distance(gal0, gal1):
    return abs(gal0[0] - gal1[0]) + abs(gal0[1] - gal1[1])

def main():
#    rows = read_map('test.txt')
    rows = read_map('input.txt')
    print(rows)
    galaxies = find_galaxies(rows)
    print(galaxies)
#    for r in range(len(rows)):
#        if is_row_empty(rows, r):
#            print('Row', r, 'is empty')
#    for c in range(len(rows[0])):
#        if is_column_empty(rows, c):
#            print('Column', c, 'is empty')
    expand_space(rows, galaxies)
    print(galaxies)
    s = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            d = distance(galaxies[i], galaxies[j])
            s += d
#            print(d)
    print(s)



if __name__ == '__main__':
    main()
