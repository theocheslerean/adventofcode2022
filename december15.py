from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

import copy

def print_cave(cave,xint=None, yint=None):
    if xint is None:
        xint = (0,len(cave[0]))
    if yint is None:
        yint = (0,len(cave))
    for line in cave[yint[0]:yint[1]+1]:
        for pos in line[xint[0]:xint[1]+1]:
            print(pos, end='')
        print('')

def findbeaconv2(sensor, beacons):
    bindex = 0
    mindist = 30
    distx, disty = 30,30
    for idx, beacon in enumerate(beacons):
        dist = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])
        if mindist > dist:
            minddist = dist
            bindex = idx
    return beacons[idx]

def covermap(cave, visited, sensor, distance):
    q = []
    q.append((sensor,0))
    dist = 0
    while q:
        pos, dist = q.pop(0)

        if dist > distance:
            return

        if pos[1]+1 < len(cave[1]) and visited[pos[0]][pos[1]+1] not in ['#']:
            q.append(([pos[0],pos[1]+1],dist+1))
            cave[pos[0]][pos[1]+1] = '#'
            visited[pos[0]][pos[1]+1] = '#'
            
        if pos[1]-1 > -1 and visited[pos[0]][pos[1]-1] not in ['#']:
            q.append(([pos[0],pos[1]-1],dist+1))
            cave[pos[0]][pos[1]-1] = '#'
            visited[pos[0]][pos[1]-1] = '#'
            
        if pos[0]+1 < len(cave) and visited[pos[0]+1][pos[1]] not in ['#']:
            q.append(([pos[0]+1,pos[1]],dist+1))
            cave[pos[0]+1][pos[1]] = '#'
            visited[pos[0]+1][pos[1]] = '#'

        if pos[0]-1 > -1 and visited[pos[0]-1][pos[1]] not in ['#']:
            q.append(([pos[0]-1,pos[1]],dist+1))
            cave[pos[0]-1][pos[1]] = '#'
            visited[pos[0]-1][pos[1]] = '#'

        # if cave[pos[1]][pos[0]] in ['S', 'B']:
        #     continue

        cave[pos[0]][pos[1]] = '#'
        visited[pos[0]][pos[1]] = '#'

def solutionv2(maxx, rowidx, sensors, distances):
    cnt = 0
    for ii in tqdm(range(maxx)):
        for i in [-ii, ii]:
            for idx in range(len(sensors)):
                if distances[idx] >= abs(rowidx-sensors[idx][1]) + abs(i-sensors[idx][0]):
                    cnt += 1
                    # print(f'{i}-#')
                    # line[i] = '#'
                    break
    # print(''.join(line))
    return cnt-1


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december15.txt')
    stream = "".join(lines).strip().split('\n')

    sensors = []
    beacons = []

    for line in stream:
        line = line.split(' ')
        sensors.append([int(line[2].split('=')[1].split(',')[0]),int(line[3].split('=')[1].split(':')[0])])
        beacons.append([int(line[8].split('=')[1].split(',')[0]),int(line[9].split('=')[1])])
    
    maxx = max(max(sensors, key=lambda y: y[0])[0], max(beacons, key=lambda y: y[0])[0])
    maxy = max(max(sensors, key=lambda y: y[1])[1], max(beacons, key=lambda y: y[1])[1])

    minx = min(min(min(sensors, key=lambda y: y[0])[0], min(beacons, key=lambda y: y[0])[0]),0)
    miny = min(min(min(sensors, key=lambda y: y[1])[1], min(beacons, key=lambda y: y[1])[1]),0)

    # cave = [['.' for j in range(maxx-minx+1)] for i in range(maxy-miny+1)]
    # line = ['.' for j in range(2*maxx)]


    # print(f'{len(cave)}-{len(cave[0])}')

    '''
        4023729 too low
        4856921 too low
    '''
    # rowidx = 10
    rowidx = 2_000_000

    distances = [abs(beacons[idx][0]-sensors[idx][0]) + abs(beacons[idx][1]-sensors[idx][1]) for idx in range(len(sensors))]
    print(distances)
    
    count = solutionv2(50_000_000, rowidx, sensors, distances)
    
    for sensor in sensors:
        if sensor[1] == rowidx:
            print(sensor)
            count -= 1

    visited = []
    for beacon in beacons:
        if beacon[1] == rowidx and beacon not in visited:
            visited.append(beacon)
            count -= 1
    print(count)
    exit()

    dccave = copy.deepcopy(cave)

    print(len(sensors))
    print(len(beacons))

    # beacon, distance = findbeacon(cave, [10,7])
    # idx = 6
    # print(sensors[idx])
    # distance = abs(beacons[idx][0]-sensors[idx][0]) + abs(beacons[idx][1]-sensors[idx][1]) - 1
    # covermap(dccave, [sensors[idx][1],sensors[idx][0]], distance)
    # print_cave(dccave)
    # exit()

    for idx, sensor in enumerate(sensors):
        beacon = beacons[idx]
        distance = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])-1
        visited = copy.deepcopy(cave)
        covermap(dccave, visited, [sensor[1],sensor[0]], distance)

    for idx in range(len(sensors)):
        dccave[sensors[idx][1]][sensors[idx][0]] = 'S'
        dccave[beacons[idx][1]][beacons[idx][0]] = 'B'

    print_cave(dccave)
    print(dccave[10])
    cnt = 0
    for pos in dccave[10]:
        if pos == '#':
            cnt+=1
    return cnt




def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december15.txt')
    stream = "".join(lines).strip().split('\n')

    sensors = []
    beacons = []

    for line in stream:
        line = line.split(' ')
        sensors.append([int(line[2].split('=')[1].split(',')[0]),int(line[3].split('=')[1].split(':')[0])])
        beacons.append([int(line[8].split('=')[1].split(',')[0]),int(line[9].split('=')[1])])
    
    maxx = max(max(sensors, key=lambda y: y[0])[0], max(beacons, key=lambda y: y[0])[0])
    maxy = max(max(sensors, key=lambda y: y[1])[1], max(beacons, key=lambda y: y[1])[1])

    minx = min(min(min(sensors, key=lambda y: y[0])[0], min(beacons, key=lambda y: y[0])[0]),0)
    miny = min(min(min(sensors, key=lambda y: y[1])[1], min(beacons, key=lambda y: y[1])[1]),0)

    # cave = [['.' for j in range(maxx-minx+1)] for i in range(maxy-miny+1)]
    # line = ['.' for j in range(2*maxx)]


    # print(f'{len(cave)}-{len(cave[0])}')

    '''
        4023729 too low
        4856921 too low
    '''
    # rowidx = 10
    rowidx = 2_000_000

    distances = [abs(beacons[idx][0]-sensors[idx][0]) + abs(beacons[idx][1]-sensors[idx][1]) for idx in range(len(sensors))]
    print(distances)
    
    count = solutionv2(50_000_000, rowidx, sensors, distances)
    
    for sensor in sensors:
        if sensor[1] == rowidx:
            print(sensor)
            count -= 1

    visited = []
    for beacon in beacons:
        if beacon[1] == rowidx and beacon not in visited:
            visited.append(beacon)
            count -= 1
    print(count)
    exit()

    dccave = copy.deepcopy(cave)

    print(len(sensors))
    print(len(beacons))

    # beacon, distance = findbeacon(cave, [10,7])
    # idx = 6
    # print(sensors[idx])
    # distance = abs(beacons[idx][0]-sensors[idx][0]) + abs(beacons[idx][1]-sensors[idx][1]) - 1
    # covermap(dccave, [sensors[idx][1],sensors[idx][0]], distance)
    # print_cave(dccave)
    # exit()

    for idx, sensor in enumerate(sensors):
        beacon = beacons[idx]
        distance = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])-1
        visited = copy.deepcopy(cave)
        covermap(dccave, visited, [sensor[1],sensor[0]], distance)

    for idx in range(len(sensors)):
        dccave[sensors[idx][1]][sensors[idx][0]] = 'S'
        dccave[beacons[idx][1]][beacons[idx][0]] = 'B'

    print_cave(dccave)
    print(dccave[10])
    cnt = 0
    for pos in dccave[10]:
        if pos == '#':
            cnt+=1
    return cnt



def solution():
    print(part1())
    print(part2())