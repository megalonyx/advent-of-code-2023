#!/usr/bin/env python3

TOTAL_SUM = 0

def read_schematic(filename, schema):
    with open(filename, 'r') as f:
        for line in f:
            schema.append(line.strip())

def scan_line(schema, line):
    global TOTAL_SUM
    indigit = False
    symbolized = False
    number = 0
    for column in range(len(schema[line])):
        c = schema[line][column]
        if c.isdigit():
            if has_adjacent_symbol(schema, line, column):
                symbolized = True
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
                number = 0
            else:
                pass
            symbolized = False
    # end of line, remaining open number needs to be used
    if indigit:
#        print(number, symbolized)
        if symbolized:
            TOTAL_SUM += number
        number = 0
        symbolized = False
    
def is_symbol(c):
    return c != '.' and not c.isdigit()

def clamp(i, mini, maxi):
    if i < mini: return mini
    if i > maxi: return maxi
    return i

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

def main():
    schema = []
#    read_schematic('test.txt', schema)
    read_schematic('input.txt', schema)
    for i in range(len(schema)):
        scan_line(schema, i)
    print(TOTAL_SUM)

if __name__ == '__main__':
    main()
