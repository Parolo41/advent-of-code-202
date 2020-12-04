import re

inputFile = open('D2P1.txt', 'r')
FileLines = inputFile.readlines();

validPasswordCount = 0

for line in FileLines:
    m = re.match('^([0-9]+)-([0-9]+) (.): (.+)$', line)
    
    firstPosition = int(m.group(1))
    secondPosition = int(m.group(2))
    reqLetter = m.group(3)
    password = m.group(4)
    
    print(f"{firstPosition}-{secondPosition} {reqLetter}: {password}")
    print(f"First position: {password[firstPosition - 1]}")
    print(f"Second position: {password[secondPosition - 1]}")
    
    firstMatch = password[firstPosition - 1] == reqLetter
    secondMatch = password[secondPosition - 1] == reqLetter
    
    if firstMatch != secondMatch:
        print("Password valid")
        validPasswordCount += 1
    else:
        print("Password invalid")

print(f"The number of valid passwords is {validPasswordCount}")