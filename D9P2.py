inputFile = open('D9P1.txt', 'r')
FileLines = inputFile.readlines();

def findWeakness(FileLines, invalidNumber):
    for i in range(len(FileLines)):
        combinedValue = int(FileLines[i])
        valueList = [int(FileLines[i])]
        
        j = i + 1
        while combinedValue < invalidNumber:
            combinedValue += int(FileLines[j])
            valueList.append(int(FileLines[j]))
            
            if(combinedValue == invalidNumber):
                valueList.sort()
                return valueList[0] + valueList[-1]
                
            j += 1

weakness = findWeakness(FileLines, 90433990)

print(f"The weakness is {weakness}")