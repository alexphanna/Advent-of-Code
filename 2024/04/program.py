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

def main():
    file = open("input.txt", "r")
    lines = list(line.replace('\n', '') for line in file.readlines())

    parts = []
    parts.extend(lines) # horizontal
    parts.extend(list("".join(line) for line in list(zip(*lines[::-1])))) # vertical
    parts.extend(get_diagonals(lines)) # diagonal
    parts.extend(get_diagonals(list(line[::-1] for line in lines))) # diagonal

    count = 0 
    for part in parts:
        count += part.count("XMAS") + part.count("SAMX")
    print(count)
        

if __name__ == "__main__":
    main()