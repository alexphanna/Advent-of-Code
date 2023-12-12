import math
def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    universe = galaxies(lines)
    
    sum = 0
    for i in range(len(universe)):
        for j in range(i + 1, len(universe)):
            sum += shortest_path(lines, universe[i][0], universe[i][1], universe[j][0], universe[j][1])
    print(sum)

# count empty columns and empty rows
def shortest_path(lines, row1, column1, row2, column2):
    empty_rows = 0
    empty_columns = 0
    for i in range(min(row1, row2), max(row1, row2) + 1):
        if row_is_empty(lines, i):
            empty_rows += 1
    for i in range(min(column1, column2), max(column1, column2) + 1):
        if column_is_empty(lines, i):
            empty_columns += 1
    return abs(row1 - row2) + empty_rows * 999999 + abs(column1 - column2) + empty_columns * 999999

def row_is_empty(lines, row):
    for i in range(len(lines[row])):
        if lines[row][i] == "#":
            return False
    return True

def column_is_empty(lines, column):
    for i in range(len(lines)):
        if lines[i][column] == "#":
            return False
    return True


def galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j] == "#"):
                galaxies.append((i, j))
    return galaxies

def expand_universe(lines):
    i = 0
    while i < len(lines):
        has_galaxy = False
        for j in range(len(lines[i])):
            if (lines[i][j] == "#"):
                has_galaxy = True
        if not has_galaxy:
            lines.insert(i + 1, ['.'] * (len(lines[0])))
            i += 1
        i += 1
    
    i = 0
    while i < len(lines[0]):
        has_galaxy = False
        for j in range(len(lines)):
            if (lines[j][i] == "#"):
                has_galaxy = True
        if not has_galaxy:
            for j in range(len(lines)):
                lines[j].insert(i, ".")
            i += 1
        i += 1

    return lines

def print_universe(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(lines[i][j], end='')
        print()

if __name__ == "__main__":
    main()