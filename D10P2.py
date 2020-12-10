inputFile = open('D10P1.txt', 'r')
FileLines = inputFile.readlines();

def countPossibleCombos(joltRatings):
    if len(joltRatings) <= 2:
        return 1
    
    possibleCombos = 0
    
    i = 1
    while i <= 3 and i < len(joltRatings):
        if joltRatings[i] - joltRatings[0] <= 3:
            possibleCombos += countPossibleCombos(joltRatings[i:])
        
        i += 1
    
    return possibleCombos

joltRatings = []

for line in FileLines:
    joltRatings.append(int(line))

joltRatings.append(0)
joltRatings.sort()
joltRatings.append(joltRatings[-1] + 3)

lastBottleneck = 0
possibleCombos = 1

for i in range(len(joltRatings) - 1):
    diff = joltRatings[i + 1] - joltRatings[i]
    
    if diff == 3:
        possibleCombos = possibleCombos * countPossibleCombos(joltRatings[lastBottleneck:i+1])
        lastBottleneck = i + 1

print(f"There are {possibleCombos} possible combinations")