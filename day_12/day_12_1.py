#!/usr/bin/env python3

def read_data(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            rows.append(parse_line(line))
    return rows

def parse_line(line):
    parts = line.strip().split(' ')
#    springs = [ c for c in parts[0] ]
    springs = parts[0]
    numbers = [ int(n) for n in parts[1].split(',') ]
    return (springs, numbers)
    
def count_groups(springs):
    ingroup = False
    groups = []
    currentgroup = 0
    for i in range(len(springs)):
        if springs[i] == '#':
            if ingroup:
                currentgroup += 1
            else:
                ingroup = True
                currentgroup = 1
        elif springs[i] == '.':
            if ingroup:
                groups.append(currentgroup)
                ingroup = False
                currentgroup = 0
            else:
                pass
        else:
            print('unknown', springs[i])
            exit(-1)
    if ingroup:
        groups.append(currentgroup)
    return groups

def replace_qmarks(springs, pos, record):
    if pos >= len(springs):
        groups = count_groups(springs)
        return 1 if groups == record else 0
    if springs[pos] == '.' or springs[pos] == '#':
        return replace_qmarks(springs, pos+1, record)
    elif springs[pos] == '?':
        left = springs[:pos]
        right = springs[pos+1:]
        s = replace_qmarks(left + '.' + right, pos+1, record)
        s += replace_qmarks(left + '#' + right, pos+1, record)
        return s

def main():
#    rows = read_data('test1.txt')
#    rows = read_data('test2.txt')
    rows = read_data('input.txt')
    total = 0
    for r in rows:
        total += replace_qmarks(r[0], 0, r[1])
    print(total)
#        print(count_groups(r[0]), r[1])
#    print(rows)
# tests:
#    replace_qmarks('???.###', 0, [1,1,3])
#    replace_qmarks('.??..??...?##.', 0, [1,1,3])
    


if __name__ == '__main__':
    main()
