inputFile = open('D3P1.txt', 'r')
FileLines = inputFile.readlines();

slopes = [
    {"xVelocity": 1, "yVelocity": 1},
    {"xVelocity": 3, "yVelocity": 1},
    {"xVelocity": 5, "yVelocity": 1},
    {"xVelocity": 7, "yVelocity": 1},
    {"xVelocity": 1, "yVelocity": 2},
]

treeCountProduct = 1

for slope in slopes:
    treeCount = 0
    xPosition = 0
    
    for yPosition in range(len(FileLines)):
        if yPosition % slope['yVelocity'] != 0:
            continue
    
        line = FileLines[yPosition]
        
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
        
        xPosition += slope['xVelocity']
    
    treeCountProduct *= treeCount
    
print(f"The product of all tree counts is {treeCountProduct}")