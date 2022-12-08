from io_ import get_file_contents

from pprint import pprint

def prio(item):
    if item >= 97:
        item -= 96
    elif item >= 65 and item < 97:
        item = item - 64 + 26
    return item

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december3.txt')
    rucksacks = "".join(lines).strip()
    rucksacks = rucksacks.split('\n')
    
    s = 0
    
    for rucksack in rucksacks:
        comp1 = rucksack[:(len(rucksack)//2)]
        comp2 = rucksack[(len(rucksack)//2):]
        
        for item in comp1:
            if item in comp2:
                break
        
        s += prio(ord(item))
        
    return s
    
    
    
    
    

def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december3.txt')
    rucksacks = "".join(lines).strip()
    rucksacks = rucksacks.split('\n')
    
    s = 0
    
    for i in range(0, len(rucksacks),3):
        r1, r2, r3 = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
        
        for item in r1:
            if item in r2:
                if item in r3:
                    break
                
        s += prio(ord(item))

    return s
    

def solution():
    print(part2())
    # print(part2())