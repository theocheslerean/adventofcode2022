from io_ import get_file_contents
import numpy as np

from pprint import pprint

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december10.txt')
    stream = "".join(lines).strip().split('\n')
    
    Xs = [1]
    val = 1
    
    for line in stream:
        com = line.split(' ')[0]
        if com == 'noop':
            Xs.append(val)
            continue
        Xs.append(val)
        Xs.append(Xs[-1])
        val = Xs[-1] + int(line.split(' ')[1])
        
    Xs.append(val)
    
    return sum([Xs[i]*(i) for i in range(20,len(Xs),40)])

def checkOverlap(spriteMiddle, cycle):
    return '#' if (spriteMiddle == (cycle % 40)) or (spriteMiddle+1 == (cycle % 40)) or (spriteMiddle-1 == (cycle % 40)) else '.'
        
def part2():
        #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december10.txt')
    stream = "".join(lines).strip().split('\n')
    
    '''
        X holds the middle of a 3px wide sprite
        CRT: 40 wide, 6 high
        top-left left-to-right pixels 0 to 39
        1 pixel per cycle
        
    
    '''
    
    Xs = [1]
    val = 1
    
    cycle = 0
    
    for line in stream:
        com = line.split(' ')[0]
        if com == 'noop':
            cycle += 1
            print(checkOverlap(val,cycle-1), end='')
            if cycle % 40 == 0:
                print('')
            # Xs.append(val)
            continue
        cycle += 1
        print(checkOverlap(val,cycle-1), end='')
        if cycle % 40 == 0:
            print('')
        
        cycle += 1
        print(checkOverlap(val,cycle-1), end='')
        if cycle % 40 == 0:
            print('')
        val = val + int(line.split(' ')[1])
        
    return sum([Xs[i]*(i) for i in range(20,len(Xs),40)])
        


def solution():
    print(part1())
    print(part2())