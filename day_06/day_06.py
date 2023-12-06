#!/usr/bin/env python3

def read_data(filename):
    races = []
    with open(filename, 'r') as f:
        timestr = f.readline().strip()
        diststr = f.readline().strip()
    times = timestr.split()
    times.pop(0)
    dists = diststr.split()
    dists.pop(0)
    times = [ int(t) for t in times ]
    dists = [ int(d) for d in dists ]
    return [ r for r in zip(times, dists) ]

def try_race(r):
    winnings = 0
    avail_time = r[0]
    dist_to_beat = r[1]
    for hold_time in range(0, avail_time+1):
        dist = (avail_time - hold_time) * hold_time
        if dist > dist_to_beat:
            winnings += 1
    return winnings

def main():
#    races = read_data('test.txt')
    races = read_data('input.txt')
#    print(races)
    margin_prod = 1
    for r in races:
        margin_prod *= try_race(r)
    print(margin_prod)

if __name__ == '__main__':
    main()
