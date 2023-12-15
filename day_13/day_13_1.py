#!/usr/bin/env python3

import numpy as np

def read_patterns(filename):
    patterns = []
    rows = []
    with open(filename, 'r') as f:
        while line := f.readline():
            line = line.strip()
            if line == '':
                patterns.append(rows)
                rows = []
            else:
                cols = [ 1 if c == '#' else 0 for c in line ]
                rows.append(cols)
    patterns.append(rows)
    return patterns

def array_from_pattern(pattern):
    arr = np.array(pattern)
    return arr

# hrow = 1 .. maxrow
def is_horizontal_reflection(arr, hrow):
    maxrow, maxcol = arr.shape
    numtoprows = hrow
    numbottomrows = maxrow - hrow
    numrows = min(numtoprows, numbottomrows)
    for r in range(0, numrows):
        for c in range(0, maxcol):
            if arr[hrow-r-1][c] != arr[hrow+r+1-1][c]:
                return False
    return True

# vcol = 1 .. maxcol
def is_vertical_reflection(arr, vcol):
    maxrow, maxcol = arr.shape
    numleftcols = vcol
    numrightcols = maxcol - vcol 
    numcols = min(numleftcols, numrightcols)
    for c in range(0, numcols):
        for r in range(0, maxrow):
            if arr[r][vcol-c-1] != arr[r][vcol+c+1-1]:
                return False
    return True

def score_for_array(arr):
    maxrow, maxcol = arr.shape
    s = 0
    for col in range(1, maxcol):
        if is_vertical_reflection(arr, col):
            s += col
    for row in range(1, maxrow):
        if is_horizontal_reflection(arr, row):
            s += 100 * row
    return s

def print_grid(grid):
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            v = grid[r, c]
            p = '.' if v == 0 else '#'
            print(p, end='')
        print()

def main():
#    patterns = read_patterns('test.txt')
    patterns = read_patterns('input.txt')
    total = 0
    for p in patterns:
        arr = array_from_pattern(p)
        score = score_for_array(arr)
        total += score
    print(total)

if __name__ == '__main__':
    main()
