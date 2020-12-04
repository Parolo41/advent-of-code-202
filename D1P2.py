def findPartsOfSum(numberOfParts, targetSum, Lines):
    i = 0
    while i < len(Lines) - (numberOfParts - 1):
        intVal = int(Lines[i])
        
        if numberOfParts > 1:
            result = findPartsOfSum(numberOfParts - 1, targetSum - intVal, Lines[i + 1:])
            
            if isinstance(result, list):
                result.append(intVal)
                return result
        else:
            if intVal == targetSum:
                return [intVal]
                
        i += 1
    return False
    
inputFile = open('D1P1.txt', 'r')
FileLines = inputFile.readlines();

parts = findPartsOfSum(3, 2020, FileLines)

if isinstance(parts, list):
    solution = 1
    
    for part in parts:
        print(part)
        solution *= part

    print("The solution is %d" % solution)
else:
    print("The solution couldn't be found")