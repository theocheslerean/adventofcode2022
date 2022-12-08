from io_ import get_file_contents

from pprint import pprint


def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december5.txt')
    procedure = "".join(lines)
    
    input_stacks, procedures = procedure.split('\n\n')
    
    input_stacks = input_stacks.split('\n')
    procedures = "".join(procedures).split('\n')
    
    stacks = [[] for i in range(len(input_stacks[-1].split('   ')))]
    
    for i in range(len(input_stacks)-2, -1, -1):
        
        line = input_stacks[i]
        
        ctr = 0
        for i in range(0,len(line),4):
            if line[i:i+3] != '   ':
                stacks[ctr].append(line[i:i+3])
            ctr += 1
            
    for proc in procedures:
        proc = proc.split(' ')
        
        howmany = int(proc[1])
        source = int(proc[3])-1
        dest = int(proc[5])-1
        
        for i in range(howmany):
            stacks[dest].append(stacks[source].pop(-1))

        
    return "".join([stack[-1] if len(stack) > 0 else '' for stack in stacks]).replace('[','').replace(']','')
    
    
    
def part2():
    #pick up multiple crates
    lines = get_file_contents('inputs/input_december5.txt')
    procedure = "".join(lines)
    
    input_stacks, procedures = procedure.split('\n\n')
    
    input_stacks = input_stacks.split('\n')
    procedures = "".join(procedures).split('\n')
    
    stacks = [[] for i in range(len(input_stacks[-1].split('   ')))]
    
    for i in range(len(input_stacks)-2, -1, -1):
        
        line = input_stacks[i]
        
        ctr = 0
        for i in range(0,len(line),4):
            if line[i:i+3] != '   ':
                stacks[ctr].append(line[i:i+3])
            ctr += 1
            
    for proc in procedures:
        proc = proc.split(' ')
        
        howmany = int(proc[1])
        source = int(proc[3])-1
        dest = int(proc[5])-1
        
        res = []
        for i in range(howmany):
            res.append(stacks[source].pop(-1))
        res.reverse()
        stacks[dest] = stacks[dest] + res

        
    return "".join([stack[-1] if len(stack) > 0 else '' for stack in stacks]).replace('[','').replace(']','')

def solution():
    print(part2())
    # print(part2())