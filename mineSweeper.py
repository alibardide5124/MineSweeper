linesCount  = 0
linesLength = 0
print("Enter lines count and lines length (Between 1 & 9)")
while linesCount  == 0 or linesCount  > 9:
    linesCount  = int(input("Enter lines count:  "))
while linesLength == 0 or linesLength > 9:
    linesLength = int(input("Enter lines length: "))

def checkMapLine(line):
    if len(line) != linesLength:
        return False
    for i in line:
        if i != '.' and i != '*':
            return False
    return True

def checkLineMines(line, currentChar):
    mines = 0
    if line[currentChar] == "*":
        mines += 1
    if currentChar != 0:
        if line[currentChar - 1] == "*":
            mines += 1
    if currentChar != linesLength - 1:
        if line[currentChar + 1] == "*":
            mines += 1
    return mines

def DotMap(lines):
    dotArray = []
    for line in lines:
        strLine = ""
        for char in line:
            strLine += char + " "
        dotArray.append(strLine)
    return dotArray

def NumMap(lines):
    numArray = []
    currentLine = 0
    for i in lines:
        currentChar = 0
        num = ""
        for char in i:
            if char == '*':
                num += "* "
                currentChar += 1
                continue
            mines = 0
            mines += checkLineMines(lines[currentLine], currentChar)
            if currentLine != 0:
                mines += checkLineMines(lines[currentLine - 1], currentChar)
            if currentLine != linesLength - 1:
                mines += checkLineMines(lines[currentLine + 1], currentChar)
            num += str(mines) + " "
            currentChar += 1
        currentLine += 1
        numArray.append(num)
    return numArray

lines = []
print("OK. You have ", linesCount, " lines and you can add ", linesLength, " characters on each line (Only write \'*\' and \'.\'... write \'*\' for mines and \'.\' for empty spaces)")
for i in range(0, linesCount):
    line = ""
    lineArray = []
    while not checkMapLine(line):
        line = input("Enter line 0" + str(i +1) + ": ")
    for i in line:
        lineArray.append(i)
    lines.append(lineArray)

print("Dot Map: ")
for i in DotMap(lines):
    print(i)

print("Num Map:")
for i in NumMap(lines):
    print(i)
