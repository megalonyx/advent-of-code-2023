#!/usr/bin/env python3

from collections import deque

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

def part1(rows, start, steps_left):
    height = len(rows)
    width = len(rows[0])
    queue = deque([(start, steps_left)])
    visited = set()
    endpoints = set()
    while queue:
        current, steps_left = queue.popleft()
        if steps_left >= 0:   # 0: reached end of this path
            if steps_left % 2 == 0:  # even: we can always reach this; odd: impossible
                endpoints.add(current)
            if steps_left > 0: # advance to next position
                steps_left -= 1
                r, c = current
                neighbours = []
                if r > 0: neighbours.append( (r-1, c) )
                if r < height-1: neighbours.append( (r+1, c) )
                if c > 0: neighbours.append( (r, c-1) )
                if c < width-1: neighbours.append( (r, c+1) )
                for neigh in neighbours:
                    r, c = neigh
                    if neigh in visited or rows[r][c] == '#':
                        continue
                    else:
                        queue.append( (neigh, steps_left) )
                        visited.add( neigh )
    return endpoints

def main():
#    rows = read_map('test.txt')
    rows = read_map('input.txt')
    start = starting_pos(rows)
    res = part1(rows, start, 64)
    print(len(res))

if __name__ == '__main__':
    main()
