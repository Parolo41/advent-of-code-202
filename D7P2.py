import re

inputFile = open('D7P1.txt', 'r')
FileLines = inputFile.readlines();

def countInnerBags(outerBag, bagIndex):
    bagCount = 0
    
    for innerBag in bagIndex[outerBag]:
        bagCount += (1 + countInnerBags(innerBag['type'], bagIndex)) * innerBag['count']
    
    return bagCount

bagIndex = {}

for line in FileLines:
    m = re.match("^(\w+ \w+) bags contain ", line)
    
    outerBag = m.group(1)
    innerBags = line[len(m.group(0)):-2].split(", ")
    
    bagIndex[outerBag] = []
    
    for innerBag in innerBags:
        if innerBag == "no other bags":
            continue
        
        m = re.match("^(\d+) (\w+ \w+) bags?$", innerBag)
        
        bagDict = { 'type': m.group(2), 'count': int(m.group(1)) }
        
        bagIndex[outerBag].append(bagDict)

print(bagIndex)

goldBagCount = countInnerBags("shiny gold", bagIndex)

print(f"There are {goldBagCount} bags inside a shiny gold bag")