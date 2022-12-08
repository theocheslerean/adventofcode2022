from io_ import get_file_contents



def part1():
    #compute points given the exact strategy guide
    lines = get_file_contents('inputs/input_december2.txt')
    games = "".join(lines)
    
    games = games.replace('X','A')
    games = games.replace('Y','B')
    games = games.replace('Z','C')
    
    points = 0
    
    for game in games.split('\n'):
        curr = 0
        op, me = game.split(' ')
        
        sign = {'A' : 1, 'B' : 2, 'C' : 3}[me]
        win = {
            'A A' : 3, 'A B' : 6, 'A C' : 0,
            'B A' : 0, 'B B' : 3, 'B C' : 6,
            'C A' : 6, 'C B' : 0, 'C C' : 3,
               }[game]

        points += sign + win
    return points
    
def part2():
    #compute points given the exact strategy guide
    lines = get_file_contents('inputs/input_december2.txt')
    games = "".join(lines)
    
    points = 0
    
    for game in games.split('\n'):
        curr = 0
        op, action = game.split(' ')
        
        win = {
            'A X' : 0, 'A Y' : 3, 'A Z' : 6,
            'B X' : 0, 'B Y' : 3, 'B Z' : 6,
            'C X' : 0, 'C Y' : 3, 'C Z' : 6,
               }[game]
        
        me = {
            'A X' : 'C', 'A Y' : 'A', 'A Z' : 'B',
            'B X' : 'A', 'B Y' : 'B', 'B Z' : 'C',
            'C X' : 'B', 'C Y' : 'C', 'C Z' : 'A',
               }[game]
        
        sign = {'A' : 1, 'B' : 2, 'C' : 3}[me]
        # win = {
        #     'A A' : 3, 'A B' : 6, 'A C' : 0,
        #     'B A' : 0, 'B B' : 3, 'B C' : 6,
        #     'C A' : 6, 'C B' : 0, 'C C' : 3,
        #        }[game]

        points += sign + win
    return points

def solution():
    print(part2())
    # print(part2())