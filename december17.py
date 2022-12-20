from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

import copy

# (string represenation, width, height, radiusx, radiusy)
rocks = [
    (['####'], 4, 1),
    (['.#.','###','.#.'], 3, 3),
    (['..#','..#','###'], 3, 3),
    (['#','#','#','#'], 1, 4),
    (['##','##'], 2, 2),
]

def updatePosition(rock, position, jet, chamber):
    # direct with jet then fall down one position if possible
    
    rock, width, height = rock
    
    
    y, x = position[0], position[1]
    
    
    '''
        4|.X@..
        3|.@@..
        2|.....
        1|.....
    
    
    '''
    
    # update left/right
    if jet == '<':
        if x-1 > -1:
            # check the whole height
            for i in range(height):
                xpos = rock[i].index('#')
                # print(f'check vertical left {rock[i][xpos]} ~ { chamber[y-i][x+xpos+1]}')
                if chamber[y-i][x+xpos-1] != '.':
                    break
            else:
                x -= 1
    
    elif jet == '>':
        if x+width < len(chamber[0]):
            # check the whole height
            for i in range(height):
                xpos = len(rock[i]) - rock[i][::-1].index('#') - 1
                # print(f'check vertical right {rock[i][xpos]} ~ { chamber[y-i][x+xpos+1]}')
                if chamber[y-i][x+xpos+1] != '.':
                    break
            else:
                x += 1
    
    # update down
    ismoved = False
    if y-height > -1:
        for j in range(width):
            # print(f'check horizontal {rock[height-1][j]} ~ {chamber[y-height+1][x+j]} ~ {chamber[y-height][x+j]}')
            if rock[height-1][j] == '.' and chamber[y-height+1][x+j] != '.':
                break
            if rock[height-1][j] == '#' and chamber[y-height][x+j] != '.':
                break
        else:
            ismoved = True
            y -= 1
            
    return [y, x], ismoved

def addRock(chamber, rock, position):
    rock, width, height = rock
    for i in range(height):
        for j in range(width):
                if rock[i][j] == '#':
                    chamber[position[0]-i][position[1]+j] = rock[i][j]

def drawChamber(chamber):
    for line in reversed(chamber):
        print("".join(line))

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december17.txt')
    stream = "".join(lines).strip()
       
    
    '''
        for time in 1..2022:
            get next rock: rock[time % 5]
            set position of rock at +3 of max height and center column
            set ismoved to True
            while ismoved:
                get next jet
                move rock with jet if possible
                move rock down if possible
                    if not possible ismoved = False
                    
        is not possible to move down
            get widht of rock and check if any of the n blocks below is occupied
            if not then move down
            if yes then break
    '''
    
    maxheight = 0
       
    chamber = [
        list('+-------+'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
    ]
    
    ctr = 0
    time = -1
    
    # maxrocks = 2217     # 3382 is too high
    maxrocks = 2022   # 3099 is too low
    # 3195 too low
    
    for ctr in tqdm(range(maxrocks)):
        rock = rocks[ctr % 5]
        
        # initialize position always topleft
        position = [maxheight+3+rock[2], 3]
        
        ismoved = True

        while ismoved:
            time += 1
            
            jet = stream[time % len(stream)]
            
            newposition, ismoved = updatePosition(rock, position, jet, chamber)

            position = newposition
            
            
            
        addRock(chamber, rock, position)
            
        # update maxheight
        diff = max(maxheight, position[0]) - maxheight
        for i in range(diff):
            chamber.append(list('|.......|'))
        maxheight += diff

        
    # drawChamber(chamber)

    return maxheight
    
    
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december17.txt')
    stream = "".join(lines).strip()
       
    
    '''
        for time in 1..2022:
            get next rock: rock[time % 5]
            set position of rock at +3 of max height and center column
            set ismoved to True
            while ismoved:
                get next jet
                move rock with jet if possible
                move rock down if possible
                    if not possible ismoved = False
                    
        is not possible to move down
            get widht of rock and check if any of the n blocks below is occupied
            if not then move down
            if yes then break
    '''
    
    maxheight = 0
       
    chamber = [
        list('+-------+'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
    ]
    
    ctr = 0
    time = -1
    
    # maxrocks = 1_000_000_000_000
    maxrocks = 1_000_000
    
    for ctr in tqdm(range(maxrocks)):
        rock = rocks[ctr % 5]
        
        # initialize position always topleft
        position = [maxheight+3+rock[2], 3]
        
        ismoved = True

        while ismoved:
            time += 1
            
            # if time % len(stream) == 0:
            #     print(f'{time} - {len(stream)} - {ctr} - {maxheight}')
            
            jet = stream[time % len(stream)]
            
            newposition, ismoved = updatePosition(rock, position, jet, chamber)

            position = newposition
            
            
            
        addRock(chamber, rock, position)
            
        # update maxheight
        diff = max(maxheight, position[0]) - maxheight
        for i in range(diff):
            chamber.append(list('|.......|'))
        maxheight += diff
        
        # print(diff, end=' ')

    
    # for idx, line in enumerate(chamber):
    #     ctr = 0
    #     for ch in list(line):
    #         if ch == '#':
    #             ctr += 1
    #     if idx % 2022 == 0:
    #         print("")
    #     print(f'{ctr}', end=' ')
    
    # drawChamber(chamber)
    return maxheight

def compute_for_n(maxrocks):
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december17.txt')
    stream = "".join(lines).strip()
    
    maxheight = 0
       
    chamber = [
        list('+-------+'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
        list('|.......|'),
    ]
    
    ctr = 0
    time = -1
    
    for ctr in tqdm(range(maxrocks)):
        rock = rocks[ctr % 5]
        
        # initialize position always topleft
        position = [maxheight+3+rock[2], 3]
        
        ismoved = True

        while ismoved:
            time += 1
            
            jet = stream[time % len(stream)]
            
            newposition, ismoved = updatePosition(rock, position, jet, chamber)

            position = newposition
            
            
            
        addRock(chamber, rock, position)
            
        # update maxheight
        diff = max(maxheight, position[0]) - maxheight
        for i in range(diff):
            chamber.append(list('|.......|'))
        maxheight += diff

    return maxheight

def part3():
    
    # Every 10091 moves (length of jet instructions) the order repeats
    # first 10091 moves have 2744 height with 1715 characters
    # next 10091 moves have 2711 height with 1715 characters and then repeat
    
    times = 1_000_000_000_000 // 1715
    rest = 1_000_000_000_000 % 1715
    
    height = times * 2711 + compute_for_n(1715+rest) - 2711
    
    return height

def solution():
    # print(part1())
    # print(part2())
    print(part3())
    
    
    
    
# 1 2 1 2 0 1 3 2 1 1 0 3 3 2 2 1 3 3 4 0 1 2 2 2 2 1 3 3 2 2 1 3 3 0 0 1 3 3 4 0 1 3 2 0 0 1 3 3 2 0 1 2 1 2 0 1 2 1 3 0 0 1 2 2 0 1 3 0 4 0 0 2 2 0 0 0 2 3 0 1 1 3 2 2 0 0 2 2 4 2 1 3 3 4 2 1 3 0 3 0 0 2 0 2 2 1 3 2 2 0 1 2 1 2 0 1 2 1 2 0 1 3 3 2 0 1 2 1 2 0 1 3 2 2 2 1 2 3 0 1 1 3 0 4 0 0 3 0 4 0 1 3 3 2 0 1 3 2 1 1 1 3 3 0 0 1 3 3 0 0 1 2 1 2 0 0 3 0 3 0 1 3 3 2 2 1 2 3 4 0 1 3 3 2 0 1 3 2 1 2 1 3 2 4 0 0 2 2 1 2 0 2 3 4 0 1 3 0 4 2 1 3 3 2 2 1 3 2 0 0 1 3 3 2 0 1 3 2 4 0 1 3 2 0 0 0 2 1 3 0 1 3 3 4 0 1 3 2 0 2 1 2 1 2 0 1 3 2 4 2 0 2 3 2 2 1 2 1 3 2 0 3 0 0 0 1 3 2 2 0 1 3 2 0 0 1 3 0 4 2 1 2 3 0 1 1 3 3 2 0 1 3 3 0 0 1 2 3 2 0 1 3 3 0 0 1 3 3 4 0 1 3 0 3 2 1 3 0 4 0 1 3 3 0 0 1 3 3 2 0 1 3 3 0 0 1 3 3 0 2 1 3 3 0 2 1 3 0 3 0 0 2 3 0 0 1 3 2 0 0 1 3 3 0 2 1 1 2 1 0 1 2 3 0 1 1 3 3 2 2 1 3 3 2 0 1 3 2 0 0 1 3 3 0 2 1 3 3 0 0 1 3 2 0 0 1 3 3 4 0 1 3 3 4 0 1 3 2 2 2 1 3 2 4 0 1 2 3 0 0 1 3 3 2 2 0 2 3 2 0 1 0 3 2 0 1 3 2 0 0 0 2 3 0 0 1 2 3 0 2 1 2 2 2 0 1 3 2 0 0 1 2 1 2 0 0 2 3 0 0 1 2 3 0 0 1 2 3 0 2 1 3 3 4 2 1 3 0 3 0 1 3 2 0 0 1 3 0 2 0 1 3 0 2 0 1 3 3 0 2 1 3 0 2 0 1 3 2 4 2 1 3 2 2 0 1 3 2 4 0 1 3 3 2 2 0 0 3 4 0 1 3 3 0 2 1 3 3 2 0 1 3 3 0 0 1 3 2 2 2 1 3 2 0 2 1 3 3 4 0 1 3 3 0 0 1 2 2 1 0 0 3 2 2 0 1 3 2 4 2 1 2 1 2 2 0 3 0 0 2 1 3 0 2 0 1 2 1 4 2 1 2 1 3 0 0 2 3 4 2 1 3 3 0 0 1 3 2 2 2 1 3 0 3 2 1 3 2 1 2 1 3 3 4 0 1 3 2 4 2 1 2 3 0 1 1 2 3 0 0 0 3 3 0 0 1 3 2 2 0 1 3 2 0 2 1 2 2 2 2 1 3 0 2 0 0 3 2 2 0 1 3 2 0 1 1 3 2 4 0 1 2 3 2 0 1 2 3 2 0 1 3 3 0 0 1 3 3 0 0 1 3 2 2 0 1 2 1 0 2 1 3 3 0 0 1 3 2 0 0 1 3 2 2 0 1 3 3 4 0 0 0 3 2 0 1 3 0 1 0 1 3 2 4 2 1 3 3 2 0 1 3 3 0 0 1 3 3 2 2 1 3 0 3 0 0 1 3 2 2 1 3 3 2 0 1 3 0 0 2 1 3 2 1 2 1 2 3 2 2 1 2 3 4 0 1 3 3 0 0 0 2 0 2 2 1 2 3 2 2 1 2 3 0 2 1 3 3 0 2 1 3 3 2 2 0 2 3 0 2 1 3 2 2 2 0 0 3 1 0 1 3 3 2 2 1 3 3 2 2 1 2 2 4 0 1 3 3 0 2 1 3 3 2 0 1 3 0 3 0 0 1 2 4 0 1 3 3 4 0 1 2 1 2 2 1 0 3 0 0 1 3 3 2 0 1 3 3 0 0 1 3 3 2 2 1 3 3 2 0 0 3 2 2 0 0 2 2 2 0 0 3 3 0 0 1 2 1 2 0 1 3 0 2 0 1 3 3 4 2 0 0 3 2 2 1 3 0 3 0 0 2 3 0 2 1 2 2 4 0 0 2 3 0 2 1 3 2 2 0 1 3 2 2 2 0 2 0 4 0 1 2 1 2 0 1 3 3 2 0 1 3 2 0 1 0 3 0 1 1 1 3 0 3 0 0 1 3 0 2 0 3 0 0 2 0 0 3 0 2 1 3 2 4 2 1 3 3 4 0 0 2 0 0 0 1 2 1 2 0 1 3 0 3 2 1 3 3 0 0 0 3 0 1 2 1 3 3 2 2 1 3 3 0 0 1 3 3 2 0 1 3 3 0 2 0 2 2 4 0 1 3 3 4 0 1 2 3 4 2 0 2 3 4 0 1 3 3 0 0 1 3 3 4 0 1 2 3 2 2 1 3 3 4 0 1 2 2 1 2 0 1 2 2 0 1 2 3 0 2 0 2 3 0 0 1 0 3 1 0 1 3 2 0 2 1 3 2 0 0 1 3 3 0 0 1 3 2 2 0 1 3 2 0 0 1 3 2 2 0 1 0 3 1 1 1 3 0 4 0 1 3 3 2 0 1 3 3 0 0 1 3 3 0 2 1 3 3 0 2 1 3 3 4 0 0 2 0 0 2 1 3 3 2 0 1 3 0 2 0 1 3 3 0 0 1 2 1 2 0 1 3 3 2 2 1 3 3 4 2 1 3 3 2 0 1 3 2 0 0 1 3 0 2 0 1 3 3 4 2 0 0 3 0 0 1 3 2 0 2 1 3 2 2 2 1 3 2 2 0 1 2 2 4 0 1 3 3 2 2 1 3 3 4 2 1 3 3 0 2 1 0 3 2 2 1 3 3 0 2 1 3 3 2 2 1 3 2 2 0 0 2 2 4 0 0 2 0 0 2 0 2 3 0 0 0 3 3 0 0 1 3 2 4 2 1 2 2 0 2 1 3 0 3 2 1 3 3 2 0 1 3 2 0 0 1 3 2 2 0 1 2 2 4 0 1 3 3 0 0 1 3 3 0 0 0 3 0 3 2 1 3 3 2 0 0 2 2 2 2 1 2 3 2 0 1 3 3 2 0 1 2 3 0 0 0 3 0 2 0 0 2 2 4 0 0 3 3 0 0 1 3 2 2 0 1 3 2 2 0 1 3 3 0 2 1 3 0 2 2 1 3 3 0 2 1 3 2 2 0 1 3 3 2 0 1 3 3 2 0 1 3 3 0 0 1 0 3 1 0 0 3 3 0 2 0 2 3 4 0 1 2 2 2 0 1 3 2 2 0 1 3 2 1 1 1 3 3 4 0 1 3 3 0 0 1 2 1 2 0 1 3 3 0 2 1 2 3 2 2 1 3 3 2 0 1 0 3 4 0 1 2 1 1 0 1 2 3 2 0 1 3 2 0 0 0 2 2 2 2 1 3 2 2 0 1 3 3 2 2 1 3 3 2 0 1 2 1 2 0 1 2 1 3 0 0 3 0 0 2 1 3 3 2 0 1 2 2 2 0 1 2 3 2 0 1 3 3 0 0 1 2 1 0 0 1 3 3 0 0 1 3 3 0 2 1 3 0 4 0 1 3 0 4 0 1 2 2 2 0 1 3 3 2 2 1 3 3 4 0 0 2 0 0 0 1 3 3 0 0 1 2 1 3 0 1 0 3 2 0 1 3 2 0 0 0 2 3 0 2 1 3 3 0 0 1 3 3 0 2 1 2 2 4 2 1 3 2 2 2 1 3 3 2 2 1 3 3 0 2 1 2 3 0 0 0 3 2 2 0 1 0 2 2 0 0 2 3 4 0 1 3 3 4 2 0 2 2 0 2 1 2 3 0 0 1 2 2 2 2 1 3 2 0 0 1 3 0 3 0 0 2 3 4 2 1 3 3 0 0 1 3 3 2 0 1 2 3 0 2 1 2 3 2 0 0 3 2 2 2 1 0 3 1 0 1 2 1 2 0 0 2 2 2 2 1 3 3 0 2 1 3 3 0 0 1 3 2 1 0 1 3 2 0 0 1 3 2 0 0 1 2 1 2 0 1 3 2 0 0 1 3 3 2 2 1 1 2 1 2 0 0 2 2 0 0 2 3 0 0 1 3 2 0 0 1 2 1 4 0 0 2 3 0 0 1 3 3 0 2 1 3 2 4 2 1 3 0 3 0 0 2 3 2 0 0 2 2 0 0 1 3 3 4 0 1 3 3 0 0 1 2 3 2 2 1 3 3 4 0 1 3 2 0 0 1 3 0 1 2 1 3 3 0 0 1 3 3 2 0 1 3 3 4 0 1 2 2 0 2 0 0 3 2 0 1 3 3 2 2 1 3 0 2 0 1 3 3 4 2 1 2 1 2 0 0 3 3 0 2 1 3 3 2 0 0 2 3 0 2 1 3 3 2 0 1 2 2 4 0 0 2 3 0 0 1 2 1 4 2 1 3 3 0 2 1 0 3 2 0 1 2 2 2 0 0 2 3 0 2 1 2 1 3 0 0 1 2 4 0 0 0 3 0 0 1 3 3 2 0 1 3 0 3 0 0 3 0 3 2 1 2 3 0 2 1 3 3 2 0 1 3 3 4 0 0 3 3 2 0 1 3 3 0 0 1 3 2 0 0 1 3 3 4 0 1 3 3 4 0 1 3 2 2 2 1 3 2 4 0 1 2 3 0 0 1 3 3 2 2 0 2 3 2 0 1 0 3 2 0 1 3 2 0 0 0 2 3 0 0 1 2 3 0 2 1 2 2 2 0 1 3 2 0 0 1 2 1 2 0 0 2 3 0 0 1 2 3 0 0 1 2 3 0 2 1 3 3 4 2 1 3 0 3 0 1 3 2 0 0 1 3 0 2 0 1 3 0 2 0 1 3 3 0 2 1 3 0 2 0 1 3 2 4 2 1 3 2 2 0 1 3 2 4 0 1 3 3 2 2 0 0 3 4 0 1 3 3 0 2 1 3 3 2 0 1 3 3 0 0 1 3 2 2 2 1 3 2 0 2 1 3 3 4 0 1 3 3 0 0 1 2 2 1 0 0 3 2 2 0 1 3 2 4 2 1 2 1 2 2 0 3 0 0 2 1 3 0 2 0 1 2 1 4 2 1 2 1 3 0 0 2 3 4 2 1 3 3 0 0 1 3 2 2 2 1 3 0 3 2 1 3 2 1 2 1 3 3 4 0 1 3 2 4 2 1 2 3 0 1 1 2 3 0 0 0 3 3 0 0 1 3 2 2 0 1 3 2 0 2 1 2 2 2 2 1 3 0 2 0 0 3 2 2 0 1 3 2 0 1 1 3 2 4 0 1 2 3 2 0 1 2 3 2 0 1 3 3 0 0 1 3 3 0 0 1 3 2 2 0 1 2 1 0 2 1 3 3 0 0 1 3 2 0 0 1 3 2 2 0 1 3 3 4 0 0 0 3 2 0 1 3 0 1 0 1 3 2 4 2 1 3 3 2 0 1 3 3 0 0 1 3 3 2 2 1 3 0 3 0 0 1 3 2 2 1 3 3 2 0 1 3 0 0 2 1 3 2 1 2 1 2 3 2 2 1 2 3 4 0 1 3 3 0 0 0 2 0 2 2 1 2 3 2 2 1 2 3 0 2 1 3 3 0 2 1 3 3 2 2 0 2 3 0 2 1 3 2 2 2 0 0 3 1 0 1 3 3 2 2 1 3 3 2 2 1 2 2 4 0 1 3 3 0 2 1 3 3 2 0 1 3 0 3 0 0 1 2 4 0 1 3 3 4 0 1 2 1 2 2 1 0 3 0 0 1 3 3 2 0 1 3 3 0 0 1 3 3 2 2 1 3 3 2 0 0 3 2 2 0 0 2 2 2 0 0 3 3 0 0 1 2 1 2 0 1 3 0 2 0 1 3 3 4 2 0 0 3 2 2 1 3 0 3 0 0 2 3 0 2 1 2 2 4 0 0 2 3 0 2 1 3 2 2 0 1 3 2 2 2 0 2 0 4 0 1 2 1 2 0 1 3 3 2 0 1 3 2 0 1 0 3 0 1 1 1 3 0 3 0 0 1 3 0 2 0 3 0 0 2 0 0 3 0 2 1 3 2 4 2 1 3 3 4 0 0 2 0 0 0 1 2 1 2 0 1 3 0 3 2 1 3 3 0 0 0 3 0 1 2 1 3 3 2 2 1 3 3 0 0 1 3 3 2 0 1 3 3 0 2 0 2 2 4 0 1 3 3 4 0 1 2 3 4 2 0 2 3 4 0 1 3 3 0 0 1 3 3 4 0 1 2 3 2 2 1 3 3 4 0 1 2 2 1 2 0 1 2 2 0 1 2 3 0 2 0 2 3 0 0 1 0 3 1 0 1 3 2 0 2 1 3 2 0 0 1 3 3 0 0 1 3 2 2 0 1 3 2 0 0 1 3 2 2 0 1 0 3 1 1 1 3 0 4 0 1 3 3 2 0 1 3 3 0 0 1 3 3 0 2 1 3 3 0 2 1 3 3 4 0 0 2 0 0 2 1 3 3 2 0 1 3 0 2 0 1 3 3 0 0 1 2 1 2 0 1 3 3 2 2 1 3 3 4 2 1 3 3 2 0 1 3 2 0 0 1 3 0 2 0 1 3 3 4 2 0 0 3 0 0 1 3 2 0 2 1 3 2 2 2 1 3 2 2 0 1 2 2 4 0 1 3 3 2 2 1 3 3 4 2 1 3 3 0 2 1 0 3 2 2 1 3 3 0 2 1 3 3 2 2 1 3 2 2 0 0 2 2 4 0 0 2 0 0 2 0 2 3 0 0 0 3 3 0 0 1 3 2 4 2 1 2 2 0 2 1 3 0 3 2 1 3 3 2 0 1 3 2 0 0 1 3 2 2 0 1 2 2 4 0 1 3 3 0 0 1 3 3 0 0 0 3 0 3 2 1 3 3 2 0 0 2 2 2 2 1 2 3 2 0 1 3 3 2 0 1 2 3 0 0 0 3 0 2 0 0 2 2 4 0 0 3 3 0 0 1 3 2 2 0 1 3 2 2 0 1 3 3 0 2 1 3 0 2 2 1 3 3 0 2 1 3 2 2 0 1 3 3 2 0 1 3 3 2 0 1 3 3 0 0 1 0 3 1 0 0 3 3 0 2 0 2 3 4 0 1 2 2 2 0 1 3 2 2 0 1 3 2 1 1 1 3 3 4 0 1 3 3 0 0 1 2 1 2 0 1 3 3 0 2 1 2 3 2 2 1 3 3 2 0 1 0 3 4 0 1 2 1 1 0 1 2 3 2 0 1 3 2 0 0 0 2 2 2 2 1 3 2 2 0 1 3 3 2 2 1 3 3 2 0 1 2 1 2 0 1 2 1 3 0 0 3 0 0 2 1 3 3 2 0 1 2 2 2 0 1 2 3 2 0 1 3 3 0 0 1 2 1 0 0 1 3 3 0 0 1 3 3 0 2 1 3 0 4 0 1 3 0 4 0 1 2 2 2 0 1 3 3 2 2 1 3 3 4 0 0 2 0 0 0 1 3 3 0 0 1 2 1 3 0 1 0 3 2 0 1 3 2 0 0 0 2 3 0 2 1 3 3 0 0 1 3 3 0 2 1 2 2 4 2 1 3 2 2 2 1 3 3 2 2 1 3 3 0 2 1 2 3 0 0 0 3 2 2 0 1 0 2 2 0 0 2 3 4 0 1 3 3 4 2 0 2 2 0 2 1 2 3 0 0 1 2 2 2 2 1 3 2 0 0 1 3 0 3 0 0 2 3 4 2 1 3 3 0 0 1 3 3 2 0 1 2 3 0 2 1 2 3 2 0 0 3 2 2 2 1 0 3 1 0 1 2 1 2 0 0 2 2 2 2 1 3 3 0 2 1 3 3 0 0 1 3 2 1 0 1 3 2 0 0 1 3 2 0 0 1 2 1 2 0 1 3 2 0 0 1 3 3 2 2 1 1 2 1 2 0 0 2 2 0 0 2 3 0 0 1 3 2 0 0 1 2 1 4 0 0 2 3 0 0 1 3 3 0 2 1 3 2 4 2 1 3 0 3 0 0 2 3 2 0 0 2 2 0 0 1 3 3 4 0 1 3 3 0 0 1 2 3 2 2 1 3 3 4 0 1 3 2 0 0 1 3 0 1 2 1 3 3 0 0 1 3 3 2 0 1 3 3 4 0 1 2 2 0 2 0 0 3 2 0 1 3 3 2 2 1 3 0 2 0 1 3 3 4 2 1 2 1 2 0 0 3 3 0 2 1 3 3 2 0 0 2 3 0 2 1 3 3 2 0 1 2 2 4 0 0 2 3 0 0 1 2 1 4 2 1 3 3 0 2 1 0 3 2 0 1 2 2 2 0 0 2 3 0 2 1 2 1 3 0 0 1 2 4 0 0 0 3 0 0 1 3 3 2 0 1 3 0 3 0 0 3 0 3 2 1 2 3 0 2 1 3 3 2 0 1 3 3 4 0 0 3 3 2 0 1 3 3 0 0 1 3 2 0 0 1 3 3 4 0 1 3 3 4 0 1 3 2 2 2 1 3 2 4 0 1 2 3 0 0 1 3 3 2 2 0 2 3 2 0 1 0 3 2 0 1 3 2 0 0 0 2 3 0 0 1 2 3 0 2 1 2 2 2 0 1 3 2 0 0 1 2 1 2 0 0 2 3 0 0 1 2 3 0 0 1 2 3 0 2 1 3 3 4 2 1 3 0 3 0 1 3 2 0 0 1 3 0 2 0 1 3 0 2 0 1 3 3 0 2 1 3 0 2 0 1 3 2 4 2 1 3 2 2 0 1 3 2 4 0 1 3 3 2 2 0 0 3 4 0 1 3 3 0 2 1 3 3 2 0 1 3 3 0 0 1 3 2 2 2 1 3 2 0 2 1 3 3 4 0 1 3 3 0 0 1 2 2 1 0 0 3 2 2 