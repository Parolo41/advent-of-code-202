import re

inputFile = open('D2P1.txt', 'r')
FileLines = inputFile.readlines();

validPasswordCount = 0

for line in FileLines:
    m = re.match('^([0-9]+)-([0-9]+) (.): (.+)$', line)
    
    minimumCount = int(m.group(1))
    maximumCount = int(m.group(2))
    reqLetter = m.group(3)
    password = m.group(4)
    
    occurrences = re.findall(reqLetter, password)
    
    print(f"{m.group(1)}-{m.group(2)} {m.group(3)}: {m.group(4)}")
    
    if len(occurrences) >= minimumCount and len(occurrences) <= maximumCount:
        print("Password valid")
        validPasswordCount += 1
    else:
        print("Password invalid")

print(f"The number of valid passwords is {validPasswordCount}")