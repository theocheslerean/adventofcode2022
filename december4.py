from io_ import get_file_contents

from pprint import pprint


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december4.txt')
    sections = "".join(lines).strip().split('\n')
    
    s = 0
    
    for section_pair in sections:
        s1, s2 = section_pair.split(',')
        
        s1_start, s1_end = s1.split('-')
        s2_start, s2_end = s2.split('-')
        
        s1_start = int(s1_start)
        s2_start = int(s2_start)
        s1_end = int(s1_end)
        s2_end = int(s2_end)       
        
        if (s1_start >= s2_start and s1_start <= s2_end) and (s1_end >= s2_start and s1_end <= s2_end) and (s1_start <= s1_end):
            # print(f's1 in s2: {s1_start} - {s1_end} : {s2_start} - {s2_end}')
            
            s += 1
            continue
        elif (s2_start >= s1_start and s2_start <= s1_end) and (s2_end >= s1_start and s2_end <= s1_end) and (s2_start <= s2_end):
            # print(f's2 in s1: {s1_start} - {s1_end} : {s2_start} - {s2_end}')
            
            s += 1
            continue

        
    return s
    
    
    
    
    

def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december4.txt')
    sections = "".join(lines).strip().split('\n')
    
    s = 0
    
    for section_pair in sections:
        s1, s2 = section_pair.split(',')
        
        s1_start, s1_end = s1.split('-')
        s2_start, s2_end = s2.split('-')
        
        s1_start = int(s1_start)
        s2_start = int(s2_start)
        s1_end = int(s1_end)
        s2_end = int(s2_end)       
        
        if (s1_start >= s2_start and s1_start <= s2_end) or (s1_end >= s2_start and s1_end <= s2_end):
            s += 1
            continue
        elif (s2_start >= s1_start and s2_start <= s1_end) or (s2_end >= s1_start and s2_end <= s1_end) and (s2_start <= s2_end):
            s += 1
            continue

        
    return s

def solution():
    print(part1())
    print(part2())