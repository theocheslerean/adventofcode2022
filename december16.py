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
    distances = [[0 for j in range(len(nodes))] for i in range(len(nodes))]
    
    for i in range(len(nodes)):
        for node in nodes[nodelist[i]]['neighbors']:
            distances[i][nodelist.index(node)] += 1

    pprint(distances)
    
def part2():
    pass

def solution():
    print(part1())
    print(part2())