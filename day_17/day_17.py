#!/usr/bin/env python3

import heapq

DOWN = (1,0)
UP = (-1,0)
LEFT = (0,-1)
RIGHT = (0,1)

def read_data(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            row = [ int(c) for c in line.strip() ]
            rows.append(row)
    return rows

def turn_left(direc):
    if direc == UP:
        return LEFT
    elif direc == LEFT:
        return DOWN
    elif direc == DOWN:
        return RIGHT
    elif direc == RIGHT:
        return UP
    else:
        print('illegal direction')
        exit(-1)
    return None

def turn_right(direc):
    if direc == UP:
        return RIGHT
    elif direc == RIGHT:
        return DOWN
    elif direc == DOWN:
        return LEFT
    elif direc == LEFT:
        return UP
    else:
        print('illegal direction')
        exit(-1)
    return None

def partX(rows, min_steps, max_steps):
    height = len(rows)
    width = len(rows[0])
    startpos = (0, 0) # row, col
    targetpos = (height-1, width-1)
    # Dijkstra:
    visited = set()
    # queue entry: ( cost, (posr, posc), (dr, dc), stepsfordir )
    # cost comes first, as heapq is sorted
    # init queue for down and right starting from start:
    queue = [ ( 0, startpos, DOWN, 0 ), ( 0, startpos, RIGHT, 0) ]
    heapq.heapify(queue)

    while queue:
        cost, pos, direc, steps = heapq.heappop(queue)
        if pos == targetpos and steps >= min_steps:
            return cost
        if (pos, direc, steps) in visited:
            continue
        visited.add( (pos, direc, steps) )

        # we now have potentially three directions to go:
        oldr, oldc = pos
        # turn left:
        dr, dc = turn_left(direc)
        newr, newc = (oldr + dr, oldc + dc)
        if steps >= min_steps and (0 <= newr < height) and (0 <= newc < width):
            newcost = cost + rows[newr][newc]
            heapq.heappush(queue, ( newcost, (newr, newc), (dr, dc), 1 ) )
        # turn right:
        dr, dc = turn_right(direc)
        newr, newc = (oldr + dr, oldc + dc)
        if steps >= min_steps and (0 <= newr < height) and (0 <= newc < width):
            newcost = cost + rows[newr][newc]
            heapq.heappush(queue, ( newcost, (newr, newc), (dr, dc), 1 ) )
        # forward:
        dr, dc = direc
        newr, newc = (oldr + dr, oldc + dc)
        if steps < max_steps and (0 <= newr < height) and (0 <= newc < width):
            newcost = cost + rows[newr][newc]
            heapq.heappush(queue, ( newcost, (newr, newc), direc, steps+1 ) )

    # if we reach this, we haven't found a way:
    print('no way found')
    exit(-1)
    return None

def main():
#    rows = read_data('test.txt')
    rows = read_data('input.txt')
    print(partX(rows, 1, 3))
    print(partX(rows, 4, 10))


if __name__ == '__main__':
    main()
