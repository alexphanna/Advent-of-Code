def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    # Find S
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start = [i, j]

    distance = 0
    prev_position = [start[0], start[1]]
    position = [start[0] - 1, start[1]]
    while True:
        distance += 1
        temp = [position[0], position[1]]
        pipe = lines[position[0]][position[1]]
        if pipe == "|":
            position[0] += position[0] - prev_position[0]
        elif pipe == "-":
            position[1] += position[1] - prev_position[1]
        elif pipe == "L":
            if position[0] == prev_position[0]:
                position[0] -= 1
            elif position[1] == prev_position[1]:
                position[1] += 1
        elif pipe == "J":
            if position[0] == prev_position[0]:
                position[0] -= 1
            elif position[1] == prev_position[1]:
                position[1] -= 1
        elif pipe == "7":
            if position[1] == prev_position[1]:
                position[1] -= 1
            elif position[0] == prev_position[0]:
                position[0] += 1
        elif pipe == "F":
            if position[0] == prev_position[0]:
                position[0] += 1
            elif position[1] == prev_position[1]:
                position[1] += 1
        elif pipe == "S":
            break
        prev_position = temp
    print(distance // 2)
        


if __name__ == "__main__":
    main()