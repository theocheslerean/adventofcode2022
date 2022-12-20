from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

import copy


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december18.txt')
    stream = "".join(lines).strip().split('\n')
    
    '''
        add cube to grid
        check all sides for neighbors
        added sides to the total number = 6 - 2 * neighbors 
    
    '''
    width = 25
    grid = [[[0 for i in range(width)] for j in range(width)] for k in range(width)]
    
    total_sum = 0
    
    for line in stream:
        line = line.split(',')
        x, y, z = int(line[0]), int(line[1]), int(line[2])
        
        opensides = 6
        
        for (xx,yy,zz) in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
            if grid[xx][yy][zz] == 1:
                opensides -= 2
        
        grid[x][y][z] = 1
        
        total_sum += opensides
    
    return total_sum
    
       
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december18.txt')
    stream = "".join(lines).strip().split('\n')
    
    '''
        add cube to grid
        check all sides for neighbors
        added sides to the total number = 6 - 2 * neighbors 
    
    '''
    width = 25
    grid = [[[0 for i in range(width)] for j in range(width)] for k in range(width)]
    visited = copy.deepcopy(grid)
    
    total_sum = 0
    
    for line in stream:
        line = line.split(',')
        x, y, z = int(line[0]), int(line[1]), int(line[2])
        
        opensides = 6
        
        for (xx,yy,zz) in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
            if grid[xx][yy][zz] == 1:
                opensides -= 2
        
        grid[x][y][z] = 1
        
        total_sum += opensides
        
    '''
        start from 0,0,0
        for all neigbors fill with 1 -> so there should be one big connected element in the graph
        the remaining 0's are inside the droplet
    '''
    pprint(grid[0])
    
    
    queue = [(0,0,0)]
    grid[0][0][0] = 1
    while queue:
        q = queue.pop(0)
        grid[q[0]][q[1]][q[2]] = 1
        if q[0]+1 < width and grid[q[0]+1][q[1]][q[2]] == 0:
            queue.append((q[0]+1,q[1],q[2]))
            grid[q[0]+1][q[1]][q[2]] = 1
        if q[0]-1 >= 0 and grid[q[0]-1][q[1]][q[2]] == 0:
            queue.append((q[0]-1,q[1],q[2]))
            grid[q[0]-1][q[1]][q[2]] = 1
        if q[1]+1 < width and grid[q[0]][q[1]+1][q[2]] == 0:
            queue.append((q[0],q[1]+1,q[2]))
            grid[q[0]][q[1]+1][q[2]] = 1
        if q[1]-1 >= 0 and grid[q[0]][q[1]-1][q[2]] == 0:
            queue.append((q[0],q[1]-1,q[2]))
            grid[q[0]][q[1]-1][q[2]] = 1
        if q[2]+1 < width and grid[q[0]][q[1]][q[2]+1] == 0:
            queue.append((q[0],q[1],q[2]+1))
            grid[q[0]][q[1]][q[2]+1] = 1
        if q[2]-1 >= 0 and grid[q[0]][q[1]][q[2]-1] == 0:
            queue.append((q[0],q[1],q[2]-1))
            grid[q[0]][q[1]][q[2]-1] = 1

    
    inner_sum = 0
    
    for x in range(width):
        for y in range(width):
            for z in range(width):
                
                if grid[x][y][z] == 0:
                
                    opensides = 6
                    
                    for (xx,yy,zz) in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
                        if visited[xx][yy][zz] == 1:
                            opensides -= 2
                    
                    visited[x][y][z] = 1
                    
                    inner_sum += opensides
    
    

    return total_sum - inner_sum
    

def solution():
    # print(part1())
    print(part2())
    