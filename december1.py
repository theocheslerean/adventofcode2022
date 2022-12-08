from io_ import get_file_contents



def part1():
    #top1
    lines = get_file_contents('inputs/input_december1.txt')
    elves = "".join(lines).split('\n\n')
    
    for i in range(len(elves)):
        elves[i] = sum([int(calories) if calories != '' else 0 for calories in elves[i].split('\n')])
    
    return max(elves)

def part2():
    #topk
    lines = get_file_contents('inputs/input_december1.txt')
    elves = "".join(lines).split('\n\n')
    
    for i in range(len(elves)):
        elves[i] = sum([int(calories) if calories != '' else 0 for calories in elves[i].split('\n')])
        
    elves.sort(reverse=True)
    
    return sum((elves[0], elves[1], elves[2]))

def solution():
    print(part1())
    print(part2())