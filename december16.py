from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

import json

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
        
    pprint(nodes)
    
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
                 

    time = 30

    ctr = 1

    nl = ['DD','BB','JJ','HH','EE','CC']

    current_node = 'AA'

    total_flow = 0

    opened = []




    # while time:
    
    #     opened.append(current_node)

    #     dist = distances[nodelist.index(current_node)]

    #     cost = [((time-dist[i]-1) if (time-dist[i]-1) >= 0 else 0) * nodes[nodelist[i]]['flow'] for i in range(len(dist))]
    #     print(f'{current_node} - {time} - {dist} - {cost}')
        
    #     for i in range(len(cost)):
    #         c = cost[i]
    #         if c == 0:
    #             continue
    #         for j in range(len(cost)):
    #             if i == j:
    #                 continue
    #             print(f"neighbor {nodelist[j]}:{nodes[nodelist[j]]['flow']}-{dist[j]}")
    #             c -= (dist[i]+1) * nodes[nodelist[i]]['flow']
    #         print(f'{nodelist[i]}:{c}')

    #     for node in opened:
    #         cost[nodelist.index(node)] = 0


    #     if max(cost) == 0:
    #         break

    #     next_index = cost.index(max(cost))
        
    #     current_node = nodelist[next_index]

    #     for k in range(dist[nodelist.index(current_node)]+1):
    #         s = 0
    #         for n in opened:
    #             s += nodes[n]['flow']
    #         print(f'{ctr}: {s}')
    #         ctr += 1

    #     time -= (dist[next_index]+1)

    #     total_flow += max(cost)
        
                
    # floyd warshall
    nl = ['DD','BB','JJ','HH','EE','CC']
    
    flow = [[0 for j in range(len(nodes))] for i in range(len(nodes))]

    time = [[30 for i in range(len(nodes))] for j in range(len(nodes))]
    
    for iteration in range(30):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                t = time[i][j]
                f = flow[i][j]
                for k in range(len(nodes)):
                    if i == k or j == k:
                        continue
                    flow[i][j] = ((time[i][j]-distances[i][j]-1) if (time[i][j]-distances[i][j]-1) >= 0 else 0) * nodes[nodelist[j]]['flow']
                    # flow_i_k = ((time-distances[i][k]-1) if (time-distances[i][k]-1) >= 0 else 0) * nodes[nodelist[k]]['flow']
                    flow_i_k_j = ((time[i][j]-distances[i][k]-distances[k][j]-1) if (time[i][j]-distances[i][k]-distances[k][j]-1) >= 0 else 0) * nodes[nodelist[j]]['flow']
                    # print(f'{nodelist[i]} - {nodelist[k]} - {nodelist[j]} : {flow[i][j]} , {flow_i_k_j}')
                    if flow[i][j] < flow_i_k_j:
                        flow[i][j] = f + flow_i_k_j
                        time[i][j] = t-distances[i][k]-distances[k][j]-1 if t-distances[i][k]-distances[k][j]-1 > 0 else 0
                    else:
                        flow[i][j] = f + flow[i][j]
                        time[i][j] = t-distances[i][j]-1 if t-distances[i][j]-1 > 0 else 0
                    # print(flow_i_j)
    pprint(nodelist[flow[nodelist.index('AA')].index(max(flow[nodelist.index('AA')]))])
    pprint(flow)
    
    nl = []
    
    for i in range(len(flow)):
        idx = flow[i].index(max(flow[i]))
        nl.append(nodelist[idx])
        for j in range(len(flow)):
            flow[j][idx] = 0
    
    time = 30
    
    print(nl)
    
    # Take the nodes from list
    while time:

        opened.append(current_node)

        dist = distances[nodelist.index(current_node)]

        cost = [((time-dist[i]-1) if (time-dist[i]-1) >= 0 else 0) * nodes[nodelist[i]]['flow'] for i in range(len(dist))]

        for node in opened:
            cost[nodelist.index(node)] = 0

        # print(f'{current_node} - {time} - {dist} - {cost}')

        if max(cost) == 0:
            break

        # next_index = cost.index(max(cost))
        current_node = nl.pop(0)

        for k in range(dist[nodelist.index(current_node)]+1):
            s = 0
            for n in opened:
                s += nodes[n]['flow']
            # print(f'{ctr}: {s}')
            ctr += 1

        # time -= (dist[next_index]+1)
        time -= (dist[nodelist.index(current_node)]+1)

        # total_flow += max(cost)
        total_flow +=cost[nodelist.index(current_node)]
    
    # 1171 too low
    
    return total_flow      




def part2():
    pass

def solution():
    print(part1())
    print(part2())