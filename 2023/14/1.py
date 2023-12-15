def main():
    file = open("input.txt", "r")
    lines = file.read().splitlines()

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    total_load = 0
    for j in range(len(lines[0])):
        column = []
        for i in range(len(lines)):
            column.append(lines[i][j])

        for i in range(0, len(column)):
            if column[i] == "O":
                k = i - 1
                while k >= 0 and column[k] == ".":
                    column[k + 1] = "."
                    column[k] = "O"
                    k -= 1

        for i in range(len(column)):
            if column[i] == "O":
                total_load += len(lines) - i
    print(total_load)

if __name__ == "__main__":
    main()