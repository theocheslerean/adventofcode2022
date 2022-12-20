from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json
import copy

    
def checkPair(left, right):
    if not left and not right:
        # print('not left and not right')
        return True
    if not left and right:
        # print('not left and right')
        return True
    if left and not right:
        # print('left and not right')
        return False
    
    headleft, headright = left.pop(0), right.pop(0)
    
    
    if type(headleft) is int and type(headright) is int:
        # print(f'checkPair int-int: {headleft} - {headright}')
        if headleft < headright:
            return True
        if headleft > headright:
            return False
        if headleft == headright:
            return checkPair(left, right)
    elif type(headleft) is list and type(headright) is list:
        # print(f'checkPair list-list: {headleft} - {headright}')
        return checkPair(headleft, headright) #and checkPair(left, right)
    elif type(headleft) is list and type(headright) is int:
        # print(f'checkPair list-int: {headleft} - {headright}')
        return checkPair(headleft, [headright]) #and checkPair(left, right)
    elif type(headleft) is int and type(headright) is list:
        # print(f'checkPair int-list: {headleft} - {headright}')
        return checkPair([headleft], headright) #and checkPair(left, right)
        
    return checkPair(left, right)


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december13.txt')
    stream = "".join(lines).strip().split('\n\n')
    
    '''
        list and lists of lists (recursive)
        
        rule 1: left <= right IN ORDER
        rule 2: rule1 on each list element + left list length <= right list length
        rule 3: int to list -> rule1 and rule2
    
        What happens if the left list is shorter but the integer values are bigger
        
        len(left) > len(right) and all left <= all right IN ORDER
        len(left) > len(right) and all left > all right NOT IN ORDER
        len(left) < len(right) and all left < all right IN ORDER
        len(left) < len(right) and all left > all right NOT IN ORDER
        
        
    '''
    
    idx = 1
    
    s = 0
    
    for pair in stream:
        pair = pair.split('\n')
        
        # print(pair)
        left = json.loads(pair[0])
        right = json.loads(pair[1])
        
        print(f'{left}\n{right}')
        c = checkPair(left,right)
        print(f'{c}\n')
        if c:
            s += idx
        idx += 1

    return s
    
        
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/test_december13.txt')
    stream = "\n".join("".join(lines).strip().split('\n\n')).split('\n')
    
    
    # print(checkPair(
    #     [[1], 4],
    #     [1, [2, [3, [4, [5, 6, 0]]]]]
    # ))
    # exit()
    stream.append('[[2]]')
    stream.append('[[6]]')
    
    for i in range(len(stream)):
        stream[i] = json.loads(stream[i])
        
    for i in range(len(stream)):
        for j in range(i+1,len(stream)):
            # print(f'{stream[i]}\n{stream[j]}')
            
            left = copy.deepcopy(stream[i])
            right = copy.deepcopy(stream[j])
            
            c = checkPair(left,right)
            # print(c, end='\n\n')
            
            if not c:
                
                stream[i], stream[j] = stream[j], stream[i]
    
    for i in range(len(stream)):
        for j in range(i+1,len(stream)):
            # print(f'{stream[i]}\n{stream[j]}')
            
            left = copy.deepcopy(stream[i])
            right = copy.deepcopy(stream[j])
            
            if not checkPair(left,right):
                
                stream[i], stream[j] = stream[j], stream[i]
    
    for i in range(len(stream)):
        for j in range(i+1,len(stream)):
            # print(f'{stream[i]}\n{stream[j]}')
            
            left = copy.deepcopy(stream[i])
            right = copy.deepcopy(stream[j])
            
            if not checkPair(left,right):
                
                stream[i], stream[j] = stream[j], stream[i]
    
    print(stream)
    
    return (stream.index([[2]])+1) * (stream.index([[6]])+1)


def solution():
    # print(part1())
    print(part2())