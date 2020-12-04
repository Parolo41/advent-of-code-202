inputFile = open('D3P1.txt', 'r')
FileLines = inputFile.readlines();

xPosition = 0
xVelocity = 3

treeCount = 0

for line in FileLines:
    xPosition %= (len(line) - 1)
    
    pointer = ''
    pointer += ' ' * xPosition
    pointer += 'v'
    
    print(pointer)
    print(line[:-1])
    
    if line[xPosition] == '#':
        treeCount += 1
        
        print("yes tree")
    else:
        print("no tree")
    print()
    
    xPosition += xVelocity
print(f"There are {treeCount} trees")

