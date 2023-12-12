import sys
def main():
    sys.setrecursionlimit(10000)
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    pipes = { "-":"─", "|":"│", "F":"┌", "7":"┐", "L":"└", "J":"┘", ".":".", "S":"S" }
    bold_pipes = { "─":"━", "│":"┃", "┌":"┏", "┐":"┓", "└":"┗", "┘":"┛" }
    all_pipes = { "┃", "━", "┏", "┓", "┗", "┛" }

    for i in range(len(lines)):
        lines[i] = list(lines[i])
        for j in range(len(lines[i])):
            lines[i][j] = pipes.get(lines[i][j]) 

    # Find S
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start = [i, j]
    
    prev_position = [start[0], start[1]]
    position = [start[0] + 1, start[1]]
    while True:
        temp = [position[0], position[1]]
        pipe = lines[position[0]][position[1]]
        if pipe == "│":
            position[0] += position[0] - prev_position[0]
        elif pipe == "─":
            position[1] += position[1] - prev_position[1]
        elif pipe == "└":
            if position[0] == prev_position[0]:
                position[0] -= 1
            elif position[1] == prev_position[1]:
                position[1] += 1
        elif pipe == "┘":
            if position[0] == prev_position[0]:
                position[0] -= 1
            elif position[1] == prev_position[1]:
                position[1] -= 1
        elif pipe == "┐":
            if position[1] == prev_position[1]:
                position[1] -= 1
            elif position[0] == prev_position[0]:
                position[0] += 1
        elif pipe == "┌":
            if position[0] == prev_position[0]:
                position[0] += 1
            elif position[1] == prev_position[1]:
                position[1] += 1
        elif pipe == "S":
            lines[position[0]][position[1]] = "┏"
            break
        prev_position = temp
        lines[prev_position[0]][prev_position[1]] = bold_pipes.get(pipe)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            temp = False
            for pipe in all_pipes:
                if lines[i][j] == pipe:
                    temp = True
            if(not temp and is_inside(lines, i, j)):
                print(lines[i][j], "at", i, j)


    f = open("output.txt", "w")
    for line in lines:
        for i in line:
            f.write(str(i))
        f.write("\n")
    f.close()

def is_inside(lines, row, column):
    count = 0
    for i in range(len(lines[0])):
        if lines[row][i] == "┃" or lines[row][i] == "┏" or lines[row][i] == "┓":
            count += 1
        #elif lines[row][i] == "┓" or lines[row][i] == "┛":
        #    count -= 1
    return count % 2 == 1

if __name__ == "__main__":
    main()