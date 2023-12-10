f = open("input.txt", "r")
lines = f.read().splitlines()

def readDrawing():
    i = 0
    cargo = []
    while "[" in lines[i]:
        for j in range(1, len(lines[i]), 4):
            if lines[i][j] != " ":
                while len(cargo) - 1 < int((j - 1) / 4):
                    cargo.append([])
                cargo[int((j - 1) / 4)].append(lines[i][j])
        i += 1
    return cargo

def isInt(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

def doProcedure():
    cargo = readDrawing()
    
    for line in lines:
        if "move" in line:
            numbers = []
            for i in line.split():
                if isInt(i):
                    numbers.append(int(i))
            
            for i in range(0, numbers[0]):
                temp = cargo[numbers[1] - 1][0]
                del cargo[numbers[1] - 1][0]
                cargo[numbers[2] - 1].insert(0 + i, temp)

    procedure = ""
    for stack in cargo:
        procedure += stack[0]

    print(procedure)
    
doProcedure()