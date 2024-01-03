#!/usr/bin/env python3

# format: (row, column) as deltas
UP = (-1, 0)
DOWN = (1, 0)
LEFT  = (0, -1)
RIGHT  = (0, 1)

DIRECTIONS = {
        'U': UP,
        'D': DOWN,
        'L': LEFT,
        'R': RIGHT
}

DIRFROMHEX = {
        '0': RIGHT,
        '1': DOWN,
        '2': LEFT,
        '3': UP
}

def read_plan(filename):
    plan = []
    with open(filename, 'r') as f:
        for line in f:
            direc, meters, color = line.strip().split()
            plan.append( (DIRECTIONS[direc], int(meters)) )
    return plan

def alternate_read_plan(filename):
    plan = []
    with open(filename, 'r') as f:
        for line in f:
            _, _, color = line.strip().split()
            meters = int(color[2:7], 16)
            direc = DIRFROMHEX[color[7]]
            plan.append( (direc, meters) )
    return plan

def grid_points_from_plan(plan):
    curr = (0,0)
    points = [curr]
    for p in plan:
        direc, meters = p
        delta = direc
        for _ in range(meters):
            curr = (curr[0] + delta[0], curr[1] + delta[1])
            points.append(curr)
    return points

def shoelace(points):
    s = 0
    for i in range(len(points)-1):
        r1, c1 = points[i]
        r2, c2 = points[i+1]
        s += r1*c2 - r2*c1
    return s / 2

def picks(points, area):
    return int(abs(area) - len(points)/2 + 1) + len(points)

def main():
    plan = read_plan('test.txt')
#    plan = read_plan('input.txt')
    gridpoints = grid_points_from_plan(plan)
    print(picks(gridpoints, shoelace(gridpoints)))

#    plan = alternate_read_plan('test.txt')
    plan = alternate_read_plan('input.txt')
    gridpoints = grid_points_from_plan(plan)
    print(picks(gridpoints, shoelace(gridpoints)))


if __name__ == '__main__':
    main()
