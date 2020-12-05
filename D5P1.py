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

highestId = 0

for line in FileLines:
    rowIndex = 0
    columnIndex = 0
    
    for i in range(len(line)):
        if line[i] == 'B':
            rowIndex += bitValues[6 - i]
        
        if line[i] == 'R':
            columnIndex += bitValues[9 - i]
    
    seatId = (rowIndex * 8) + columnIndex
    
    if seatId > highestId:
        highestId = seatId

print(f"The highest seat ID equals {highestId}")