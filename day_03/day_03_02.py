#!/usr/bin/env python3

TOTAL_SUM = 0
GEARS = {} 

def read_schematic(filename, schema):
    with open(filename, 'r') as f:
        for line in f:
            schema.append(line.strip())

def scan_line(schema, line):
    global TOTAL_SUM, GEARS
    indigit = False
    symbolized = False
    geared = False
    number = 0
    gearposes = set()
    for column in range(len(schema[line])):
        c = schema[line][column]
        if c.isdigit():
            if has_adjacent_symbol(schema, line, column):
                symbolized = True
            gearpos = has_adjacent_gearsymbol(schema, line, column)
            if gearpos:
                geared = True
                gearposes.add(gearpos)
            if indigit:
                number = number * 10 + int(c)
            else:
                # new number starts
                indigit = True
                number = int(c)
        else:
            if indigit:
                # number ends
                indigit = False
#                print(number, symbolized)
                if symbolized:
                    TOTAL_SUM += number
                if geared:
                    for gearp in gearposes:
                        if gearp in GEARS:
                            GEARS[gearp].append(number)
                        else:
                            GEARS[gearp] = [number]
                        gearposes = set()
                number = 0
            else:
                pass
            symbolized = False
    # end of line, remaining open number needs to be used
    if indigit:
#        print(number, symbolized)
        if symbolized:
            TOTAL_SUM += number
        if geared:
            for gearp in gearposes:
                if gearp in GEARS:
                    GEARS[gearp].append(number)
                else:
                    GEARS[gearp] = [number]
    
def is_symbol(c):
    return c != '.' and not c.isdigit()

def is_gear_symbol(c):
    return c == '*'

def clamp(i, mini, maxi):
    if i < mini: return mini
    if i > maxi: return maxi
    return i

def has_adjacent_gearsymbol(schema, line, column):
    # check all 8 possible positions, do not cross boundary
    MAX_LINE = len(schema)-1
    MAX_COL = len(schema[line])-1
    for l in range(-1,2):
        for c in range(-1,2):
            check_l = clamp(line+l, 0, MAX_LINE)
            check_c = clamp(column+c, 0, MAX_COL)
            if is_gear_symbol(schema[check_l][check_c]):
                return (check_l, check_c)
    return False

def has_adjacent_symbol(schema, line, column):
    # check all 8 possible positions, do not cross boundary
    MAX_LINE = len(schema)-1
    MAX_COL = len(schema[line])-1
    for l in range(-1,2):
        for c in range(-1,2):
            check_l = clamp(line+l, 0, MAX_LINE)
            check_c = clamp(column+c, 0, MAX_COL)
            if is_symbol(schema[check_l][check_c]):
                return True
    return False

def count_gears():
    s = 0
    for key in GEARS:
        if len(GEARS[key]) == 2:
            s += GEARS[key][0] * GEARS[key][1]
    return s

def main():
    schema = []
#    read_schematic('test.txt', schema)
    read_schematic('input.txt', schema)
    for i in range(len(schema)):
        scan_line(schema, i)
    print(count_gears())

if __name__ == '__main__':
    main()
