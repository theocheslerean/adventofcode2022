from io_ import get_file_contents

from pprint import pprint


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december6.txt')
    stream = "".join(lines).strip()
    
    for i in range(0,len(stream)-4):
        
        curr = set(stream[i:i+4])
        

        
        if len(curr) == 4:
            print(curr)
            break
        
    return i+4
    
    
    
    
    
    
    

def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december6.txt')
    stream = "".join(lines).strip()
    
    k = 14
    
    for i in range(0,len(stream)-k):
        
        curr = set(stream[i:i+k])
        

        
        if len(curr) == k:
            print(curr)
            break
        
    return i+k
    

def solution():
    print(part1())
    print(part2())