inputFile = open('D9P1.txt', 'r')
FileLines = inputFile.readlines();

i = 25

combinationFound = False

while i < len(FileLines):
    combinationFound = False
    
    j = i - 25
    while j < i:
        k = j + 1
        while k < i:
            if int(FileLines[j]) + int(FileLines[k]) == int(FileLines[i]):
                print(f"{int(FileLines[j])} + {int(FileLines[k])} = {int(FileLines[i])}")
                combinationFound = True
                break
            
            k += 1
        if combinationFound:
            break
        
        j += 1
    if not combinationFound:
        break
    
    i += 1

print(f"{FileLines[i][:-1]} on line {i} is invalid")