from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

def print_cave(cave,xint, yint):
    if xint is None:
        xint = (0,len(cave[0]))
    if yint is None:
        yint = (0,len(cave))
    for line in cave[yint[0]:yint[1]+1]:
        for pos in line[xint[0]:xint[1]+1]:
            print(pos, end='')
        print('')

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december14.txt')
    stream = "".join(lines).strip().split('\n')
    
    cave = [['.' for i in range(550)] for j in range(200)]

    # print_cave(cave, (494,503),(0,9))

    for line in stream:
        positions = line.split(' -> ')
        for i in range(1,len(positions)):
            currx, curry = positions[i].split(',')
            prevx, prevy = positions[i-1].split(',')
            currx, curry = int(currx), int(curry)
            prevx, prevy = int(prevx), int(prevy)

            if currx < prevx:
                currx, prevx = prevx, currx

            if curry < prevy:
                curry, prevy = prevy, curry

            for i in range(prevx, currx+1):
                for j in range(prevy,curry+1):
                    cave[j][i] = '#'

    # cave[8][501] = '#'
    # cave[8][500] = '#'
    # cave[7][500] = '#'
    # cave[8][499] = '#'
    # print_cave(cave, (494,503),(0,9))

    i = 0
    while True:
        i += 1
        move = True
        sand = [0,500]

        while move:
            move = False
            if sand[0] == len(cave)-1:
                return i-1
            if cave[sand[0]+1][sand[1]] == '.':
                sand[0] += 1
                move = True
                continue
            if cave[sand[0]+1][sand[1]] in ['o','#']:
                if cave[sand[0]+1][sand[1]-1] == '.':
                    sand[0] += 1
                    sand[1] -= 1
                    move = True
                    continue
                elif cave[sand[0]+1][sand[1]+1] == '.':
                    sand[0] += 1
                    sand[1] += 1
                    move = True
                    continue
                else:
                    cave[sand[0]][sand[1]] = 'o'
                    continue
        
        # print_cave(cave, (494,503),(0,9))



    '''
        gp down
            if not possible
                go to left
                    if not possible
                        go to right
                            if not possible stay up
    '''

    
        
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december14.txt')
    stream = "".join(lines).strip().split('\n')
    

    # print_cave(cave, (494,503),(0,9))

    maxx, maxy = -1, -1
    for line in stream:
        positions = line.split(' -> ')
        for i in range(len(positions)):
            currx, curry = positions[i].split(',')
            currx, curry = int(currx), int(curry)
            if maxx < currx:
                maxx = currx
            if maxy < curry:
                maxy = curry

    # print(maxy)
    cave = [['.' for i in range(maxx+300)] for j in range(maxy+3)]
# 



    for line in stream:
        positions = line.split(' -> ')
        for i in range(1,len(positions)):
            currx, curry = positions[i].split(',')
            prevx, prevy = positions[i-1].split(',')
            currx, curry = int(currx), int(curry)
            prevx, prevy = int(prevx), int(prevy)

            if currx < prevx:
                currx, prevx = prevx, currx

            if curry < prevy:
                curry, prevy = prevy, curry

            for i in range(prevx, currx+1):
                for j in range(prevy,curry+1):
                    cave[j][i] = '#'

    for i in range(len(cave[0])):
        cave[maxy+2][i] = '#'

    # print_cave(cave, (400,600),(0,maxy+3))
    

    # print_cave(cave, (400,600),(0,maxy+3))
    
    i = 0
    while True:
        i += 1
        move = True
        sand = [0,500]

        while move:
            move = False
            if cave[sand[0]+1][sand[1]] == '.':
                sand[0] += 1
                move = True
                continue
            if cave[sand[0]+1][sand[1]] in ['o','#']:
                if cave[sand[0]+1][sand[1]-1] == '.':
                    sand[0] += 1
                    sand[1] -= 1
                    move = True
                    continue
                elif cave[sand[0]+1][sand[1]+1] == '.':
                    sand[0] += 1
                    sand[1] += 1
                    move = True
                    continue
                else:
                    if sand[0] == 0 and sand[1] == 500:
                        print_cave(cave, (400,600),(0,maxy+3))

                        return i
                    cave[sand[0]][sand[1]] = 'o'
                    continue
        




    '''
        gp down
            if not possible
                go to left
                    if not possible
                        go to right
                            if not possible stay up
    '''
def solution():
    print(part1())
    print(part2())