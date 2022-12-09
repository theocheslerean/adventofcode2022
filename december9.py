from io_ import get_file_contents
import numpy as np

from pprint import pprint

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december9.txt')
    stream = "".join(lines).strip().split('\n')
    
    '''
        Solution 1: have a grid of visited positions and update with a 1 when the tail was there
        Solution 2: have a list of positions and don't make a grid since we don't know how wide and high it should be
            - start at (0,0) -> add (0,0) to visited
            - movement of head based on starting position
                - besides 
                    - move to a diagonal place => tail does not move
                - diagonal
                    - move away from tail => tail moves diagonally
                    - move towards tail => tail stays in place
    '''
    
    H = [0,0]
    T = [0,0]
    
    visited = set()
    visited.add(tuple(T))
    
    for instruction in stream:
        dir, dist = instruction.split(' ')[0], int(instruction.split(' ')[1])
        
        # print(f'{dir} {dist}')
        
        for i in range(dist):
            
            if dir == 'L':
                H[0] -= 1
            elif dir == 'R':
                H[0] += 1
            elif dir == 'D':
                H[1] -= 1
            elif dir == 'U':
                H[1] += 1
                
            # print(f"head: {H}")

        
            if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
                # print(f'{H}-{T}')
                continue
                # do nothing
            
            # compute direction vector
            movement = (H[0] - T[0], H[1] - T[1])
            
            # print(f"vector: {movement}")
            
            if movement[0]**2 + movement[1]**2 <= 2:
                # print(f'{H}-{T}')
                continue
            
            T[0] += movement[0] + (-1 if dir == 'R' else 1 if dir == 'L' else 0)
            T[1] += movement[1] + (-1 if dir == 'U' else 1 if dir == 'D' else 0)
            
            # print(f'{H}-{T}')
            
            visited.add(tuple(T))


    print(len(visited))
    # print((visited))
    # for i in range(len(stream)):
    #     stream[i] = [int(letter) for letter in stream[i]]

    
def part2():
    pass

def solution():
    print(part1())
    print(part2())