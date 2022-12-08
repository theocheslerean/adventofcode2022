from io_ import get_file_contents

from pprint import pprint

class Dir():
    def __init__(self, name) -> None:
        self.size = 0
        self.parent = None
        self.name = name
        self.filelist = []
        self.dirlist = []

    def __init__(self, name, parent) -> None:
        self.size = 0
        self.parent = parent
        self.name = name
        self.filelist = []
        self.dirlist = []
        
    def cd(self, name):
        if name == '..':
            return self.parent
        else:
            for dir in self.dirlist:
                if dir.name == name:
                    return dir
                
    def updatesize(self):
        curr = self
        while curr is not None:
            curr.size += self.filelist[-1].size
            curr = curr.parent
            
    def pwd(self):
        s = []
        curr = self
        while curr is not None:
            s.insert(0, curr.name)
            curr = curr.parent
        return '/'.join(s)
    
    def __str__(self):
        s = (self.parent.name if self.parent is not None else '') + '/' + self.name + '\n'
        for dir in self.dirlist:
            s = s + f'  dir {dir.name}\n'
        for file in self.filelist:
            s = s + f'  {file}'
        return s
        
        
class File():
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        
    def __str__(self):
        return f'{self.name} {self.size}\n'

def findsmalldirs(dir):
    result = []
    q = [dir]
    while q:
        curr = q.pop(0)
        for d in curr.dirlist:
            q.append(d)
        if curr.size <= 100000:
            result.append(curr)
    return result

def generateviabledirs(dir, s):
    result = []
    q = [dir]
    while q:
        curr = q.pop(0)
        for d in curr.dirlist:
            q.append(d)
        if curr.size + 70_000_000 - s >= 30_000_000:
            result.append((curr,curr.size + 70_000_000 - s))
    return result

def part1():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/test_december7.txt')
    stream = "".join(lines).strip().split('\n')
    
    currdir = Dir('/', None)
    
    root = currdir
    
    i = 1
    while i < len(stream):
        tokens = stream[i].split(' ')
        
        if tokens[0] == '$':
            if tokens[1] == 'ls':
                i += 1
                tokens = stream[i].split(' ')
                while tokens[0] != '$':
                    if tokens[0] == 'dir':
                        currdir.dirlist.append(Dir(name=tokens[1], parent=currdir))
                    elif tokens[0].isnumeric():
                        currdir.filelist.append(File(tokens[1], int(tokens[0])))
                        currdir.updatesize()
                    i += 1
                    if i == len(stream):
                        break
                    tokens = stream[i].split(' ')
            elif tokens[1] == 'cd':
                currdir = currdir.cd(tokens[2])
                i += 1
                
                
    smalldirs = findsmalldirs(root)
    
    return sum([dir.size for dir in smalldirs])
    

def part2():
    #do the towers of hanoi style
    lines = get_file_contents('inputs/input_december7.txt')
    stream = "".join(lines).strip().split('\n')
    
    currdir = Dir('/', None)
    
    root = currdir
    
    i = 1
    while i < len(stream):
        tokens = stream[i].split(' ')
        
        if tokens[0] == '$':
            if tokens[1] == 'ls':
                i += 1
                tokens = stream[i].split(' ')
                while tokens[0] != '$':
                    if tokens[0] == 'dir':
                        currdir.dirlist.append(Dir(name=tokens[1], parent=currdir))
                    elif tokens[0].isnumeric():
                        currdir.filelist.append(File(tokens[1], int(tokens[0])))
                        currdir.updatesize()
                    i += 1
                    if i == len(stream):
                        break
                    tokens = stream[i].split(' ')
            elif tokens[1] == 'cd':
                currdir = currdir.cd(tokens[2])
                i += 1
                
                
    smalldirs = generateviabledirs(root, root.size)
    
    m = smalldirs[0]
    
    for i in range(1,len(smalldirs)):
        if m[1] > smalldirs[i][1]:
            m = smalldirs[i]
            
    
    return m[0].size
    
    

def solution():
    print(part1())
    print(part2())