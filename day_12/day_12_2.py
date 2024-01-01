#!/usr/bin/env python3

from functools import cache

def read_data(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            rows.append(parse_line(line))
    return rows

def parse_line(line):
    parts = line.strip().split(' ')
    springs = '?'.join([parts[0]] * 5)
    numbers = tuple( [ int(n) for n in parts[1].split(',') ] * 5 )
    return (springs, numbers)
    
@cache
def recurse(springs, records, tally):
    if not records:
        return 0 if '#' in springs else 1
    current, records = records[0], records[1:]
    for i in range(len(springs) - sum(records) - len(records) - current + 1):
        if '#' in springs[:i]:
            break
        nxt = i + current
        if nxt <= len(springs) and '.' not in springs[i:nxt] and springs[nxt:nxt+1] != '#':
            tally += recurse(springs[nxt+1:], records, 0)
    return tally
    
def main():
#    rows = read_data('test1.txt')
#    rows = read_data('test2.txt')
    rows = read_data('input.txt')
    total = 0
    for i, r in enumerate(rows):
        total += recurse(r[0], r[1], 0)
    print(total)


if __name__ == '__main__':
    main()
