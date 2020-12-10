inputFile = open('D8P1.txt', 'r')
FileLines = inputFile.readlines();

lineExecOrder = []
i = 0
accumulator = 0

while i not in lineExecOrder:
    instruction = FileLines[i].split()
    lineExecOrder.append(i)
    
    if instruction[0] == 'jmp':
        i += int(instruction[1])
    elif instruction[0] == 'acc':
        accumulator += int(instruction[1])
        i += 1
    elif instruction[0] == 'nop':
        i += 1

print(f"Line {i} has repeated and the accumulator is at {accumulator}")