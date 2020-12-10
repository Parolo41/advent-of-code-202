inputFile = open('D8P1.txt', 'r')
FileLines = inputFile.readlines();

changedLines = []

i = 0

while i < len(FileLines):
    lineExecOrder = []
    lineChanged = False
    
    i = 0
    accumulator = 0

    while i not in lineExecOrder:
        if i >= len(FileLines):
            break;
        
        instruction = FileLines[i].split()
        lineExecOrder.append(i)
        
        if not lineChanged and i not in changedLines:
            changedLines.append(i)
            lineChanged = True
            
            print(f"Line {i} changed")
            
            if instruction[0] == 'jmp':
                instruction[0] = 'nop'
            elif instruction[0] == 'nop':
                instruction[0] = 'jmp'
        
        if instruction[0] == 'jmp':
            i += int(instruction[1])
        elif instruction[0] == 'acc':
            accumulator += int(instruction[1])
            i += 1
        elif instruction[0] == 'nop':
            i += 1

print(f"The code has terminated with line {changedLines[-1]} changed and the accumulator is at {accumulator}")