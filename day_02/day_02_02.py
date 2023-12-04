#!/usr/local/bin/python3

import re

maxes = {'red': 12, 'green': 13, 'blue': 14}

def read_games(filename):
    games = []
    with open(filename) as f:
        for line in f:
            sub = line.strip().split(': ')
            gamenr = int(sub[0].split(' ')[1])
            drawstr = sub[1]
            draws = []
            for d in drawstr.split('; '):
                draw = parse_draw(d)
                draws.append(draw)
            games.append({'number': gamenr, 'draws': draws})
    return games

def parse_draw(drawstr):
    res = {}
    dice = drawstr.split(', ')
    for d in dice:
        e = d.split(' ')
        res[e[1]] = int(e[0])
    return res

def is_game_possible(game):
    for draw in game['draws']:
        for key in draw:
            if draw[key] > maxes[key]:
                return False
    return True

def minimum_for_game_possible(game):
    mins = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game['draws']:
        for key in draw:
            if draw[key] > mins[key]:
                mins[key] = draw[key]
    return mins['red'] * mins['green'] * mins['blue']

def main():
#    games = read_games('test.txt')
    games = read_games('input.txt')
#    print(games)
    s = 0
    for i in range(len(games)):
        s += minimum_for_game_possible(games[i])
    print(s)

if __name__ == '__main__':
    main()
