inputFile = open('D10P1.txt', 'r')
FileLines = inputFile.readlines();

joltRatings = []

for line in FileLines:
    joltRatings.append(int(line))

joltRatings.append(0)
joltRatings.sort()
joltRatings.append(joltRatings[-1] + 3)

oneDiffCount = 0
threeDiffCount = 0

for i in range(len(joltRatings) - 1):
    diff = joltRatings[i + 1] - joltRatings[i]
    
    if diff == 1:
        oneDiffCount += 1
    if diff == 3:
        threeDiffCount += 1

print(f"1 diff: {oneDiffCount}, 3 diff: {threeDiffCount}, product: {oneDiffCount * threeDiffCount}")