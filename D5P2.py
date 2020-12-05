inputFile = open('D5P1.txt', 'r')
FileLines = inputFile.readlines();

bitValues = {
    0: 1,
    1: 2,
    2: 4,
    3: 8,
    4: 16,
    5: 32,
    6: 64,
}

seatIds = []

for line in FileLines:
    rowIndex = 0
    columnIndex = 0
    
    for i in range(len(line)):
        if line[i] == 'B':
            rowIndex += bitValues[6 - i]
        
        if line[i] == 'R':
            columnIndex += bitValues[9 - i]
    
    seatIds.append((rowIndex * 8) + columnIndex)

seatIds.sort()

prevId = -1

for seatId in seatIds:
    if seatId - prevId > 1 and prevId != -1:
        print(f"My seat ID is {prevId + 1}")
        exit()
    
    prevId = seatId

print("Couldn't find seat")