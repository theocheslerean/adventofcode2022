from io_ import get_file_contents
import numpy as np

from pprint import pprint

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december8.txt')
    stream = "".join(lines).strip().split('\n')

    for i in range(len(stream)):
        stream[i] = [int(letter) for letter in stream[i]]

    arr = np.array(stream)

    '''
        we need to check left->right right-> left up->down and down->up if the current max heigh stricktly smaller than the next tree is
    '''

    visited = np.zeros_like(arr).astype(np.int)
    scores = np.ones_like(arr).astype(np.int)

    count = arr.shape[0] * 2 + (arr.shape[1] - 2) * 2

    for i in range(1,arr.shape[0]-1):
        maxheight = arr[i,0]
        for j in range(1,arr.shape[1]-1):
            if arr[i,j] > maxheight and visited[i,j] != 1:
                count += 1
                visited[i,j] = 1
            if arr[i,j] > maxheight:
                maxheight = arr[i,j]
    for i in range(1,arr.shape[0]-1):
        maxheight = arr[i,-1]
        for j in range(arr.shape[1]-1,0,-1):
            if arr[i,j] > maxheight and visited[i,j] != 1:
                count += 1
                visited[i,j] = 1
            if arr[i,j] > maxheight:
                maxheight = arr[i,j]

    for j in range(1,arr.shape[0]-1):
        maxheight = arr[0,j]
        for i in range(1,arr.shape[1]-1):
            if arr[i,j] > maxheight and visited[i,j] != 1:
                count += 1
                visited[i,j] = 1
            if arr[i,j] > maxheight:
                maxheight = arr[i,j]
    for j in range(1,arr.shape[0]-1):
        maxheight = arr[-1,j]
        for i in range(arr.shape[1]-1,0,-1):
            if arr[i,j] > maxheight and visited[i,j] != 1:
                count += 1
                visited[i,j] = 1
            if arr[i,j] > maxheight:
                maxheight = arr[i,j]

    return count

def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december8.txt')
    stream = "".join(lines).strip().split('\n')

    for i in range(len(stream)):
        stream[i] = [int(letter) for letter in stream[i]]

    arr = np.array(stream)

    visited = np.zeros_like(arr).astype(np.int)
    scores = np.ones_like(arr).astype(np.int)

    count = arr.shape[0] * 2 + (arr.shape[1] - 2) * 2

    #trivial solution checmk for each location all the neighbors until a bigger value is encouintered
    for i in range(1,arr.shape[0]-1):
        for j in range(1,arr.shape[1]-1):
            curr = arr[i,j]
            ctr = 0
            for jj in range(j-1,-1,-1):
                ctr += 1
                if arr[i,jj] >= curr:
                    break
            scores[i,j] *= ctr

    for i in range(1,arr.shape[0]-1):
        for j in range(1,arr.shape[1]-1):
            curr = arr[i,j]
            ctr = 0
            for jj in range(j+1,arr.shape[1]):
                ctr += 1
                if arr[i,jj] >= curr:
                    break
            scores[i,j] *= ctr

    for j in range(1,arr.shape[1]-1):
        for i in range(1,arr.shape[0]-1):
            curr = arr[i,j]
            ctr = 0
            for ii in range(i-1,-1,-1):
                ctr += 1
                if arr[ii,j] >= curr:
                    break
            scores[i,j] *= ctr

    for j in range(1,arr.shape[1]-1):
        for i in range(1,arr.shape[0]-1):
            curr = arr[i,j]
            ctr = 0
            for ii in range(i+1,arr.shape[0]):
                ctr += 1
                if arr[ii,j] >= curr:
                    break
            scores[i,j] *= ctr

    return np.max(scores)





    # Solution with finding the rolling maximum per row an dcolumn.
    # Doesn't work for the case where you have a decreasing sequence since trhe last maximum is farther than the highest visible tree
    # for i in range(1,arr.shape[0]-1):
    #     maxheight = arr[i,0]
    #     maxindex = 0
    #     for j in range(1,arr.shape[1]-1):
    #         if arr[i,j] > maxheight:
    #             scores[i,j] *= abs(j)
    #         else:
    #             scores[i,j] *= abs(j - maxindex)
    #         print(f'l->r: ({i},{j}): {arr[i,j]} / {scores[i,j]}')

    #         if arr[i,j] >= maxheight:
    #             maxheight = arr[i,j]
    #             maxindex = j
    # print(scores)
    # for i in range(1,arr.shape[0]-1):
    #     maxheight = arr[i,-1]
    #     maxindex = arr.shape[1]-1
    #     for j in range(arr.shape[1]-1,0,-1):
    #         if arr[i,j] > maxheight:
    #             scores[i,j] *= abs(arr.shape[1]-1 - j)
    #         else:
    #             scores[i,j] *= abs(maxindex - j)
    #         print(f'r->l: ({i},{j}): {arr[i,j]} / {scores[i,j]}')

    #         if arr[i,j] > maxheight:
    #             maxheight = arr[i,j]
    #             maxindex = j
    # print(scores)

    # for j in range(1,arr.shape[0]-1):
    #     maxheight = arr[i,0]
    #     maxindex = 0
    #     for i in range(1,arr.shape[1]-1):
    #         if arr[i,j] > maxheight:
    #             scores[i,j] *= abs(i)
    #         else:
    #             scores[i,j] *= abs(i - maxindex)
    #         print(f'u->d: ({i},{j}): {arr[i,j]} / {scores[i,j]}')

    #         if arr[i,j] > maxheight:
    #             maxheight = arr[i,j]
    #             maxindex = i
    # print(scores)
    # for j in range(1,arr.shape[1]-1):
    #     maxheight = arr[i,-1]
    #     maxindex = arr.shape[1]-1
    #     for i in range(arr.shape[1]-1,0,-1):
    #         if arr[i,j] > maxheight:
    #             scores[i,j] *= abs(arr.shape[0]-1 - j)
    #             print(f'd->u: ({i},{j}): {arr[i,j]} / {scores[i,j]}')
    #         else:
    #             scores[i,j] *= abs(maxindex - j)

    #         if arr[i,j] > maxheight:
    #             maxheight = arr[i,j]
    #             maxindex = j
    # print(scores)

    # return count
    

def solution():
    print(part1())
    print(part2())