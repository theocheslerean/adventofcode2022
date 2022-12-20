from io_ import get_file_contents
import numpy as np

from pprint import pprint

from tqdm import tqdm

ops = {
    '*.': lambda x, y : x * x,
    '*' : lambda x, y : x * y,
    '+' : lambda x, y : x + y,
}

ops_inv = {
    '*.': lambda x, y : int(np.sqrt(x)),
    '*' : lambda x, y : x // y,
    '+' : lambda x, y : x - y,
}

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/test_december11.txt')
    stream = "".join(lines).strip().split('\n')
    
    monkeys = []
    
    for line in stream:
        line = line.strip().split(':')
        
        if line[0].split(' ')[0] == 'Monkey':
            currentMonkey = int(line[0].split(' ')[1])
            monkeys.append({
                'name' : currentMonkey,
                'items' : [],
                'operation' : {},
                'operation-inv' : {},
                'test' : {},
                'throw' : {},
                'op-y' : None,
                'test-y' : None,
                'inspected' : 0,
            })
        elif line[0].split(' ')[0] == 'Starting':
            monkeys[currentMonkey]['items'] = monkeys[currentMonkey]['items'] + [int(worryLevel) for worryLevel in line[1].split(', ')]
            
        elif line[0].split(' ')[0] == 'Operation':
            op = line[1].strip().split(' ')[3]
            if op == '*' and line[1].strip().split(' ')[4] == 'old':
                monkeys[currentMonkey]['operation'] = ops['*.']
                monkeys[currentMonkey]['operation-inv'] = ops_inv['*.']
            else:
                monkeys[currentMonkey]['op-y'] = int(line[1].strip().split(' ')[4])
                monkeys[currentMonkey]['operation'] = ops[op]
                monkeys[currentMonkey]['operation-inv'] = ops_inv[op]

        elif line[0].split(' ')[0] == 'Test':
            monkeys[currentMonkey]['test-y'] = int(line[1].strip().split(' ')[2])
            monkeys[currentMonkey]['test'] = lambda x, y: x % y == 0
            
        elif line[0] == 'If true':
            monkeys[currentMonkey]['throw'][True] = int(line[1].strip().split(' ')[3])
        elif line[0] == 'If false':
            monkeys[currentMonkey]['throw'][False] = int(line[1].strip().split(' ')[3])
    
    # pprint(monkeys)
    
    for round in range(20):
        for monkey in monkeys:
            if not(monkey['items']):
                continue              
            
            while monkey['items']:
                currentItem = monkey['items'].pop(0)
                monkey['inspected'] += 1
                # print(currentItem, end=' ')
                currentItem = monkey['operation'](currentItem, monkey['op-y'])
                # print(currentItem, end=' ')
                
                currentItem = currentItem // 3
                # print(currentItem, end=' ')
                # print(monkey['test'](currentItem, monkey['test-y']), end=' ')
                # print(monkey['throw'][monkey['test'](currentItem, monkey['test-y'])])
                
                monkeys[monkey['throw'][monkey['test'](currentItem, monkey['test-y'])]]['items'].append(currentItem)
                
                # print(currentItem)
    
    
    # pprint(monkeys)
    
    max1, max2 = -1,-1
    
    # Find max two monkeys
    insp = [monkey['inspected'] for monkey in monkeys]
    
    print(insp)
    insp.sort()
    
    return insp[-1] * insp[-2]
    
    
        
def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december11.txt')
    stream = "".join(lines).strip().split('\n')
    
    monkeys = []
    
    for line in stream:
        line = line.strip().split(':')
        
        if line[0].split(' ')[0] == 'Monkey':
            currentMonkey = int(line[0].split(' ')[1])
            monkeys.append({
                'name' : currentMonkey,
                'items' : [],
                'operation' : {},
                'operation-inv' : {},
                'test' : {},
                'throw' : {},
                'op-y' : None,
                'test-y' : None,
                'inspected' : 0,
                'sign' : None
            })
        elif line[0].split(' ')[0] == 'Starting':
            monkeys[currentMonkey]['items'] = monkeys[currentMonkey]['items'] + [int(worryLevel) for worryLevel in line[1].split(', ')]
            
        elif line[0].split(' ')[0] == 'Operation':
            op = line[1].strip().split(' ')[3]
            if op == '*' and line[1].strip().split(' ')[4] == 'old':
                monkeys[currentMonkey]['sign'] = '*.'
                monkeys[currentMonkey]['operation'] = ops['*.']
                monkeys[currentMonkey]['operation-inv'] = ops_inv['*.']
            else:
                monkeys[currentMonkey]['sign'] = op
                monkeys[currentMonkey]['op-y'] = int(line[1].strip().split(' ')[4])
                monkeys[currentMonkey]['operation'] = ops[op]
                monkeys[currentMonkey]['operation-inv'] = ops_inv[op]

        elif line[0].split(' ')[0] == 'Test':
            monkeys[currentMonkey]['test-y'] = int(line[1].strip().split(' ')[2])
            monkeys[currentMonkey]['test'] = lambda x, y: x % y == 0
            
        elif line[0] == 'If true':
            monkeys[currentMonkey]['throw'][True] = int(line[1].strip().split(' ')[3])
        elif line[0] == 'If false':
            monkeys[currentMonkey]['throw'][False] = int(line[1].strip().split(' ')[3])
    
    # pprint(monkeys)
    
    for round in tqdm(range(10000)):
        for monkey in monkeys:
            if not(monkey['items']):
                continue           
            
            nrOfItems = len(monkey['items'])
            
            while monkey['items']:
                currentItem = monkey['items'].pop(0)
                monkey['inspected'] += 1
                # print(currentItem, end=' ')
                
                currentItem = monkey['operation'](currentItem, monkey['op-y'])
                # print(currentItem, end=' ')
                
                # currentItem = currentItem // nrOfItems
                # print(currentItem, end=' ')
                # print(monkey['test'](currentItem, monkey['test-y']), end=' ')
                # print(monkey['throw'][monkey['test'](currentItem, monkey['test-y'])])
                
                # normalizedCurrentItem = int(currentItem * (1/monkey['test-y'] if monkey['test'](currentItem, monkey['test-y']) else (monkey['test-y']-1)/monkey['test-y']) // nrOfItems)
                # normalizedCurrentItem = int((currentItem * (1/monkey['test-y'] if monkey['test'](currentItem, monkey['test-y']) else (monkey['test-y']-1)/monkey['test-y'])) * nrOfItems)
                # normalizedCurrentItem = int((currentItem * (1/monkey['test-y'] if monkey['test'](currentItem, monkey['test-y']) else (monkey['test-y']-1)/monkey['test-y'])) / 2)
                # normalizedCurrentItem = int((currentItem * (1/monkey['test-y'] if monkey['test'](currentItem, monkey['test-y']) else (monkey['test-y']-1)/monkey['test-y'])) // 2)
                # normalizedCurrentItem = int(currentItem * ((monkey['test-y']-1)/monkey['test-y'] if monkey['test'](currentItem, monkey['test-y']) else 1/monkey['test-y']) * nrOfItems)
                
                            
                # monkeys[monkey['throw'][monkey['test'](currentItem, monkey['test-y'])]]['items'].append(normalizedCurrentItem)
                # monkeys[monkey['throw'][monkey['test'](currentItem, monkey['test-y'])]]['items'].append((normalizedCurrentItem))
                
                normalizedCurrentItem = currentItem % (2*3*5*7*11*13*17*19)
                # normalizedCurrentItem = currentItem % (13*17*19*23)
                # normalizedCurrentItem = currentItem % monkey['test-y'] #if currentItem % monkey['test-y'] != 0 else 0
                # normalizedCurrentItem = monkey['operation'](currentItem % monkey['test-y'] + monkey['test-y'], monkey['op-y']) % monkey['test-y']
                # normalizedCurrentItem = monkey['operation'](currentItem % monkey['test-y'], monkey['op-y'] % monkey['test-y'] if monkey['sign'] != '*.' else 1) #if currentItem % monkey['test-y'] != 0 else currentItem
                # print(f'{currentItem} - {normalizedCurrentItem}')
                
                
                monkeys[monkey['throw'][monkey['test'](currentItem, monkey['test-y'])]]['items'].append(normalizedCurrentItem)
                
                # print(currentItem)
    
    
    # pprint(monkeys)
    
    max1, max2 = -1,-1
    
    # Find max two monkeys
    insp = [monkey['inspected'] for monkey in monkeys]
    
    print(insp)
    insp.sort()
    
    return insp[-1] * insp[-2]

def part3():
    # arr = np.array([
    #     [0,0,1/23,22/23],
    #     [1/19,0,18/19,0],
    #     [0,1/13,0,12/13],
    #     [1/17,16/17,0,0],
    # ])
    
    arr = np.array([
        [-1,-1,1/23,22/23],
        [1/19,-1,18/19,-1],
        [-1,1/13,-1,12/13],
        [1/17,16/17,-1,-1],
    ])
    
    arr2 = np.array(arr)
    
    for i in range(100):
        arr2 = arr.dot(arr2)
        
    print(arr2)

def solution():
    # part3()
    # print(part1())
    print(part2())