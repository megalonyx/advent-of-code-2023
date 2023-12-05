#!/usr/bin/env python3

def read_data(filename):
    maps = {}
    with open(filename, 'r') as f:
        maps['seeds'] = read_seeds(f)
        maps['seed-to-soil'] = read_map(f)
        maps['soil-to-fertilizer'] = read_map(f)
        maps['fertilizer-to-water'] = read_map(f)
        maps['water-to-light'] = read_map(f)
        maps['light-to-temperature'] = read_map(f)
        maps['temperature-to-humidity'] = read_map(f)
        maps['humidity-to-location'] = read_map(f)
    return maps

def read_seeds(f):
    line = f.readline().strip()
    sub = line.split(': ')
    seeds = sub[1].split(' ')
    line = f.readline() # advance
    return [ int(s) for s in seeds ]
    
def read_map(f):
    themap = []
    # skip description line
    line = f.readline()
    line = f.readline()
    if line:
        line = line.strip()
    while line and len(line) > 0:
        nums = [ int(n) for n in line.split(' ') ]
        themap.append(tuple(nums))
        line = f.readline()
        if line:
            line = line.strip()
    return themap
 
def do_mapping(from_number, themap):
    dest_number = from_number
    for mapping in themap:
        source_start = mapping[1]
        source_end = source_start + mapping[2] - 1
        dest_start = mapping[0]
        if source_start <= from_number and from_number <= source_end:
            dest_number = from_number - source_start + dest_start
    return dest_number

def fully_map_seed(maps, seed):
    number = do_mapping(seed, maps['seed-to-soil'])
    number = do_mapping(number, maps['soil-to-fertilizer'])
    number = do_mapping(number, maps['fertilizer-to-water'])
    number = do_mapping(number, maps['water-to-light'])
    number = do_mapping(number, maps['light-to-temperature'])
    number = do_mapping(number, maps['temperature-to-humidity'])
    number = do_mapping(number, maps['humidity-to-location'])
    return number
    
def find_lowest_location(maps, seeds):
    minloc = fully_map_seed(maps, seeds[0])
    for seed in seeds:
        loc = fully_map_seed(maps, seed)
        minloc = min(minloc, loc)
    return minloc

def main():
#    maps = read_data('test.txt')
    maps = read_data('input.txt')
    number = maps['seeds'][0]
    loc = find_lowest_location(maps, maps['seeds'])
    print(loc)

if __name__ == '__main__':
    main()
