def get_diagonals(word_search):
    diagonals = []
    for i in range(len(word_search)):
        diagonal = ""
        for j in range(len(word_search[0])):
            if i + j < len(word_search):
                diagonal += word_search[i + j][j]
        diagonals.append(diagonal)
    for j in range (1, len(word_search[0])):
        diagonal = ""
        for i in range(len(word_search)):
            if i + j < len(word_search[0]):
                diagonal += word_search[i][j + i]
        diagonals.append(diagonal)
    return diagonals

def part_one():
    file = open("input.txt", "r")
    lines = list(line for line in file.read().split("\n"))

    parts = []
    parts.extend(lines) # horizontal
    parts.extend(list("".join(line) for line in list(zip(*lines[::-1])))) # vertical
    parts.extend(get_diagonals(lines)) # diagonal
    parts.extend(get_diagonals(list(line[::-1] for line in lines))) # diagonal

    count = 0 
    for part in parts:
        count += part.count("XMAS") + part.count("SAMX")
    print(count)

def is_x(word_search, i, j):
    word1 = word_search[i][j] + word_search[i + 1][j + 1] + word_search[i + 2][j + 2]
    word2 = word_search[i][j + 2] + word_search[i + 1][j + 1] + word_search[i + 2][j]

    return (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM")

def part_two():
    file = open("input.txt", "r")
    lines = list(line for line in file.read().split("\n"))

    count = 0
    for i in range(len(lines) - 2):
        for j in range(len(lines[i]) - 2):
            if is_x(lines, i, j):
                count += 1
    print(count)

        

if __name__ == "__main__":
    part_two()