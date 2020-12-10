import re

inputFile = open('D7P1.txt', 'r')
FileLines = inputFile.readlines();

def countOuterBags(innerBag, bagIndex, checkedBags = []):
    if innerBag in checkedBags:
        return 0
    
    checkedBags.append(innerBag)
    
    if innerBag not in bagIndex:
        return 1
    
    bagCount = 1
    
    for outerBag in bagIndex[innerBag]:
        bagCount += countOuterBags(outerBag, bagIndex, checkedBags)
    
    return bagCount

bagIndex = {}

for line in FileLines:
    m = re.match("^(\w+ \w+) bags contain ", line)
    
    outerBag = m.group(1)
    innerBags = line[len(m.group(0)):-2].split(", ")
    
    for innerBag in innerBags:
        if innerBag == "no other bags":
            continue
        
        m = re.match("^(\d+) (\w+ \w+) bags?$", innerBag)
        
        if m.group(2) not in bagIndex:
            bagIndex[m.group(2)] = []
        
        if outerBag not in bagIndex[m.group(2)]:
            bagIndex[m.group(2)].append(outerBag)

goldBagCount = countOuterBags("shiny gold", bagIndex) - 1

print(f"There are {goldBagCount} bags that can contain a shiny gold bag")