def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    previous_line = -1
    sum = 0
    for k in range(len(lines)):
        if (lines[k] == ""):
            columns = []
            for i in range(len(lines[previous_line + 1:k])):
                column = ""
                for j in range(len(lines[previous_line + 1:k][0])):
                    column += lines[previous_line + 1:k][i][j]
                columns.append(column)
            if not is_mirrored(columns) is None:
                sum += is_mirrored(columns) * 100

            rows = []
            for j in range(len(lines[previous_line + 1:k][0])):
                row = ""
                for i in range(len(lines[previous_line + 1:k])):
                    row += lines[previous_line + 1:k][i][j]
                rows.append(row)
            if not is_mirrored(rows) is None:
                sum += is_mirrored(rows)
            previous_line = k
    print(sum)

def is_mirrored(groups):
    for i in range(len(groups) - 1):
        group = i + 1
        j = i + 1
        mirrored = True
        while True:
            if (groups[i] != groups[j]):
                mirrored = False
                break
            if (0 < i and j < len(groups) - 1):
                i -= 1
                j += 1
            else:
                break
        if (mirrored):
            return group

if __name__ == "__main__":
    main()