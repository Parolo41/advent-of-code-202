import re

def isYearValid(year, minYear, maxYear):
    return int(year) >= minYear and int(year) <= maxYear

def isHeightValid(height):
    m = re.match("^(\d+)(cm|in)$", height)
    
    if m:
        heightVal = int(m.group(1))
        
        if m.group(2) == 'cm' and heightVal >= 150 and heightVal <= 193:
            return True
            
        if m.group(2) == 'in' and heightVal >= 59 and heightVal <= 76:
            return True
    return False

def isHairColorValid(hairColor):
    return bool(re.match("^#[0-9a-f]{6}$", hairColor))

def isEyeColorValid(eyeColor):
    return bool(re.match("^(?:amb|blu|brn|gry|grn|hzl|oth)$", eyeColor))

def isPidValid(pid):
    return bool(re.match("^\d{9}$", pid))

def isValid(passport):
    
    requiredFields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    
    for field in requiredFields:
        if field not in passport:
            print("Passport is not valid")
            return False
    
    return isYearValid(passport['byr'], 1920, 2002) and isYearValid(passport['iyr'], 2010, 2020) and isYearValid(passport['eyr'], 2020, 2030) and isHeightValid(passport['hgt']) and isHairColorValid(passport['hcl']) and isEyeColorValid(passport['ecl']) and isPidValid(passport['pid'])

inputFile = open('D4P1.txt', 'r')
FileLines = inputFile.readlines();

passport = {}
validPassportCount = 0

for line in FileLines:
    if len(line) <= 1:
        print(passport)
        if isValid(passport):
            print("Passport is valid")
            validPassportCount += 1
        passport = {}
        continue
    
    print(line)
    fields = re.findall("(\w{3}):((?:\w|#)+)", line)
    
    for field in fields:
        passport[field[0]] = field[1]

if passport:
    print(passport)
    if isValid(passport):
        print("Passport is valid")
        validPassportCount += 1

print(f"The number of valid passports is {validPassportCount}")