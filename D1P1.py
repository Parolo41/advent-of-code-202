def getSolution(Lines):
    i = 0
    while i < len(Lines) - 1:
        intVal1 = int(Lines[i])
        
        j = i + 1
        while j < len(Lines):
            intVal2 = int(Lines[j])
            
            if (intVal1 + intVal2) == 2020:
                print("%d + %d = %d" % (intVal1, intVal2, intVal1 + intVal2))
            
                return intVal1 * intVal2
            
            j += 1
        i += 1
    print("Couldn't find solution")
    return False
    
inputFile = open('D1P1.txt', 'r')
FileLines = inputFile.readlines();

solution = getSolution(FileLines)

if isinstance(solution, int):
    print("The solution is %d" % solution)