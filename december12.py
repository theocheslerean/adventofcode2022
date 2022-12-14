from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import queue




def neighbors(i,j,maxi,maxj):
    
    ngs = []
    if j > 0:
        ngs.append((i,j-1))
    if j < maxj-1:
        ngs.append((i,j+1))
    if i > 0:
        ngs.append((i-1,j))
    if i < maxi-1:
        ngs.append((i+1,j))
        
    return ngs
    
    
    
    

def dijkstra(graph, source, target):
    
    maxi = len(graph)
    maxj = len(graph[0])
    
    dist = [[np.inf for j in range(len(graph[0]))] for i in range(len(graph))]
    prev = [[None for j in range(len(graph[0]))] for i in range(len(graph))]
    
    q = queue.PriorityQueue()
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i == 0 and j == 0:
                continue
            q.put((np.inf, (i,j)))
    dist[source[0]][source[1]] = 0
    q.put((0, source))
    
    while not q.empty():
        prio, pos = q.get()
        
        # pprint(dist)
        
        i, j = pos[0],pos[1]
        
        for neighbor in neighbors(i,j,maxi,maxj):
            ii, jj = neighbor[0], neighbor[1]
            if graph[ii][jj] - graph[i][j] > 1:
                continue
            alt = dist[i][j] + 1
            if alt < dist[ii][jj]:
                dist[ii][jj] = alt
                prev[ii][jj] = (i,j)
                q.put((alt, (ii,jj)))
                
    return dist[target[0]][target[1]]

        
def dijkstra_inv(graph, source, target):
        
    maxi = len(graph)
    maxj = len(graph[0])
    
    dist = [[np.inf for j in range(len(graph[0]))] for i in range(len(graph))]
    prev = [[None for j in range(len(graph[0]))] for i in range(len(graph))]
    
    q = queue.PriorityQueue()
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i == 0 and j == 0:
                continue
            q.put((np.inf, (i,j)))
    dist[source[0]][source[1]] = 0
    q.put((0, source))
    
    while not q.empty():
        prio, pos = q.get()
        
        # pprint(dist)
        
        i, j = pos[0],pos[1]
        
        for neighbor in neighbors(i,j,maxi,maxj):
            ii, jj = neighbor[0], neighbor[1]
            
            if graph[ii][jj] - graph[i][j] > 1:
                continue
            
            if graph[ii][jj] == 0:
                return dist[i][j] + 1
            
            alt = dist[i][j] + 1
            if alt < dist[ii][jj]:
                dist[ii][jj] = alt
                prev[ii][jj] = (i,j)
                q.put((alt, (ii,jj)))
                
    return dist[target[0]][target[1]]
    


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/test_december12.txt')
    stream = "".join(lines).strip().split('\n')
    
    Si, Sj, Ei, Ej = 0,0,0,0
    
    for i in range(len(stream)):
        for j in range(len(stream[0])):
            if stream[i][j] == 'S':
                Si = i
                Sj = j
            if stream[i][j] == 'E':
                Ei = i
                Ej = j
                
    # print(f'{Si},{Sj}-{Ei},{Ej}')
    
    heights = {key : idx for idx,key in enumerate('abcdefghijklmnopqrstuvwxyz')}
    
    graph = [[(heights[pos] if pos not in ['S','E'] else heights['a'] if pos == 'S' else heights['z']) for pos in line] for line in stream]
    
    # print(graph)
    
    # return dijkstra(graph, (0,0), (2,5))
    return dijkstra(graph, (Si,Sj), (Ei,Ej))
    
    
        
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december12.txt')
    stream = "".join(lines).strip().split('\n')
    
    Si, Sj, Ei, Ej = 0,0,0,0
    
    for i in range(len(stream)):
        for j in range(len(stream[0])):
            if stream[i][j] == 'S':
                Si = i
                Sj = j
            if stream[i][j] == 'E':
                Ei = i
                Ej = j
                
    # print(f'{Si},{Sj}-{Ei},{Ej}')
    
    heights = {key : -idx for idx,key in enumerate('abcdefghijklmnopqrstuvwxyz')}
    
    graph = [[(heights[pos] if pos not in ['S','E'] else heights['a'] if pos == 'S' else heights['z']) for pos in line] for line in stream]
    
    # print(graph)
    
    # return dijkstra(graph, (0,0), (2,5))
    return dijkstra_inv(graph, (Ei,Ej), (Si,Sj))

def solution():
    print(part1())
    print(part2())