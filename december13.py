from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

def checkListInternal(left, right):
    
    print(f'checkListInternal: {left}-{right}')
    
    if not left or not right:
        return True
    
    # both lists have at least length 1
    headleft, headright = left.pop(0), right.pop(0)
    if type(headleft) is int and type(headright) is int:
        if headleft > headright:
            return False
        if headleft < headright:
            return True
    elif type(headleft) is list and type(headright) is list:
        if not checkListInternal(headleft,headright):
            return False
    elif type(headleft) is int and type(headright) is list:
        if not checkListInternal([headleft], headright):
            return False
    elif type(headleft) is list and type(headright) is int:
        if not checkListInternal(headleft, [headright]):
            return False
    return checkListInternal(left,right)
    
# def checkPairMixed(left, right):
    
#     print(f'checkPairMixed: {left}-{right}')
    
#     if not left and not right:
#         return True
    
#     if not left:
#         return True
    
#     if not right:
#         return False
    
#     headleft, headright = left.pop(0), right.pop(0)
    
#     if type(headleft) is int and type(headright) is int:
#         if headleft > headright:
#             return False
#     elif type(headleft) is int and type(headright) is list:
#         if not checkListInternal([headleft], headright):
#             return False
#     elif type(headleft) is list and type(headright) is int:
#         if not checkListInternal(headleft, [headright]):
#             return False
        
    # if len(left) == len(right) and len(left) == 0:
    #     if type(headright) is list:
    #         if not checkPairMixed([headleft], headright):
    #             return False
    #     elif type(headleft) is list:
    #         if not checkPairMixed(headleft, [headright]):
    #             return False
    #     elif headleft > headright:
    #         return False
    # elif not left:
    #     # if type(headright) is list:
    #     #     if not checkPairMixed([headleft], headright):
    #     #         return False
    #     if headleft > headright:
    #         return False
    # elif not right:
    #     # if type(headleft) is list:
    #     #     if not checkPairMixed(headleft, [headright]):
    #     #         return False
    #     if headleft > headright:
    #         return False
    
    return True

def checkPairSame(left, right):
    print(f'checkPairSame: {left}-{right}')
    if type(left) == type(right) and type(left) is int:
        if left > right:
            return False
        if left < right:
            return True
    elif type(left) == type(right) and type(left) is list:
        if len(left) !=0 and len(right) == 0:
            return False
        elif not checkList(left, right):
            return False
    elif type(left) == int and type(right) == list:
        # if len(right) == 0:
        #         return False
        if not checkList([left], right):
            return False
    elif type(left) == list and type(right) == int:
        # if len(left) == 0:
        #     return False
        if not checkList(left, [right]):
            return False
    return True

def checkList(left, right):
    
    # print(f'checkList: {left}-{right}')
    
    
    if not left and not right:
        # print('not left and not right')
        return True    
    
    # Check if lists have elements
    if not left and right:
        # print('not left and right')
        return True
    
    if left and not right:
        # print('left and not right')
        return False
    
    
    
    headleft, headright = left.pop(0), right.pop(0)
    
    print(f'checkList: {headleft}-{headright}')
    
    
    if type(headleft) == type(headright) and type(headleft) is int:
        if headleft > headright:
            return False
        if headleft < headright:
            return True
    elif type(headleft) == type(headright) and type(headleft) is list:
        if len(headleft) !=0 and len(headright) == 0:
            return False
        elif not checkList(headleft, headright):
            return False
    elif type(headleft) == int and type(headright) == list:
        # if len(right) == 0:
        #         return False
        if not checkList([headleft], headright):
            return False
    elif type(headleft) == list and type(headright) == int:
        # if len(left) == 0:
        #     return False
        if not checkList(headleft, [headright]):
            return False
    
    # if not checkPairSame(headleft, headright):
    #     return False
    
    return checkList(left, right)
    



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
        
        len(left) >= len(right) and all left <= all right IN ORDER
        len(left) > len(right) and all left > all right NOT IN ORDER
        len(left) < len(right) and all left < all right IN ORDER
        len(left) < len(right) and all left > all right NOT IN ORDER
        
        
    '''
    
    # print(checkPair([[[],[2,3]]], [[], 3]))
    # exit()
    
    idx = 1
    
    s = 0
    
    for pair in stream:
        pair = pair.split('\n')
        
        print(pair)
        left = json.loads(pair[0])
        right = json.loads(pair[1])
        
        print(f'{left}\n{right}')
        c = checkList(left,right)
        print(f'{c}\n')
        if c:
            s += idx
        
        
        idx += 1
        # print(idx)
        
        
        # if type(left) == type(right) and type(left) is list:
            
    return s
    
        
def part2():
    pass
def solution():
    print(part1())
    print(part2())