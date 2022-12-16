from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

def compute_cost(nodes, nodelist, start):
    return 

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/test_december16.txt')
    stream = "".join(lines).strip().split('\n')
    
    
    '''
        graph of the pipes
        compute all distances from all nodes to any other nodes
        
        at each step
            decrease the time
            compute cost for all nodes: cost_to_arrive_at_node + remaining_time * flow
            cost_to_arrive_at_node : distance
    
    '''
    
    nodes = {}
    nodelist = []
    # parse nodes
    for line in stream:
        line = line.split(' ')
        idx = line.index('to')+2
        nodelist.append(line[1])
        nodes[line[1]] = {
            'flow' : int(line[4].split('=')[1].split(';')[0]),
            'neighbors' : [line[i].strip(',') for i in range(idx, len(line))]
        }
        
    
    # compute all distances
    distances = [[np.inf for j in range(len(nodes))] for i in range(len(nodes))]
    
    for i in range(len(nodelist)):
        distances[i][i] = 0
        for neighbor in nodes[nodelist[i]]['neighbors']:
            distances[i][nodelist.index(neighbor)] = 1

    for k in range(len(nodelist)):
        for i in range(len(nodelist)):
            for j in range(len(nodelist)):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                

    # pprint(distances)

    time = 30

    ctr = 1

    nl = ['DD','BB','JJ','HH','EE','CC']

    current_node = 'AA'

    total_flow = 0

    opened = []

    # while time:

    #     opened.append(current_node)

    #     dist = distances[nodelist.index(current_node)]

    #     cost = [((time-dist[i]) if (time-dist[i]) >= 0 else 0) * nodes[nodelist[i]]['flow'] for i in range(len(dist))]

    #     for node in opened:
    #         cost[nodelist.index(node)] = 0

    #     print(f'{current_node} - {time} - {dist} - {cost}')

    #     if max(cost) == 0:
    #         break

    #     next_index = cost.index(max(cost))

    #     current_node = nl.pop(0)
    #     # current_node = nodelist[next_index]

    #     for k in range(dist[next_index]):
    #         s = 0
    #         for n in opened:
    #             s += nodes[n]['flow']
    #         print(f'{ctr}: {s}')
    #         ctr += 1

    #     time -= (dist[next_index])

    #     total_flow += max(cost)


    while time:

        opened.append(current_node)

        dist = distances[nodelist.index(current_node)]

        cost = [nodes[nodelist[i]]['flow'] - dist[i] - 1 for i in range(len(dist))]

        for node in opened:
            cost[nodelist.index(node)] = 0

        print(f'{current_node} - {time} - {dist} - {cost}')

        # if max(cost) == 0:
        #     break

        next_index = cost.index(max(cost))

        current_node = nodelist[next_index]

        for k in range(dist[next_index]+1):
            s = 0
            for n in opened:
                s += nodes[n]['flow']
            print(f'{ctr}: {s}')
            ctr += 1

        time -= (dist[next_index]+1)

        for k in range(dist[next_index]+1):
            for node in opened:
                total_flow += nodes[node]['flow']


    # while nl:

    #     opened.append(current_node)

    #     next_node = nl.pop(0)

    #     dist = distances[nodelist.index(current_node)][nodelist.index(next_node)]

    #     cost = ((time-dist-1) if (time-dist-1) >= 0 else 0) * nodes[next_node]['flow']

    #     print(f'{current_node} - {time} - {dist} - {cost}')

    #     for k in range(dist+1):
    #         s = 0
    #         for n in opened:
    #             s += nodes[n]['flow']
    #         print(f'{ctr}: {s}')
    #         ctr += 1

    #     time -= (dist+1)

    #     total_flow += cost

    #     current_node = next_node

    return total_flow

def part2():
    pass

def solution():
    print(part1())
    print(part2())