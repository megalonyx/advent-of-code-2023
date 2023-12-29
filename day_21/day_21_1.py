#!/usr/bin/env python3

#import numpy as np

STEPS_TO_REACH = 64

def read_map(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            rows.append(line.strip())
    return rows

def starting_pos(rows):
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            if rows[r][c] == 'S':
                return (r, c)
    return None

def do_step(rows, pos, stepnumber, accum):
    if stepnumber == STEPS_TO_REACH:
        accum.add( pos )
        return
    r, c = pos
    # north:
    if r > 0 and rows[r-1][c] != '#':
        do_step(rows, (r-1, c), stepnumber+1, accum)
    # south:
    if r < len(rows)-1 and rows[r+1][c] != '#':
        do_step(rows, (r+1, c), stepnumber+1, accum)
    # west:
    if c > 0 and rows[r][c-1] != '#':
        do_step(rows, (r, c-1), stepnumber+1, accum)
    # east:
    if c < len(rows[0])-1 and rows[r][c+1] != '#':
        do_step(rows, (r, c+1), stepnumber+1, accum)

def main():
#    rows = read_map('test.txt')
    rows = read_map('input.txt')
    start = starting_pos(rows)
#    print(start)
    accum = set()
    do_step(rows, start, 0, accum)
    print(len(accum))




if __name__ == '__main__':
    main()
