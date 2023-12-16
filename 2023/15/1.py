def main():
    sequences = open("input.txt", "r").readline().split(",")

    sum = 0
    for i in range(len(sequences)):
        current_value = 0
        for j in range(len(sequences[i])):
            current_value = (current_value + ord(sequences[i][j])) * 17 % 256
        sum += current_value

    print(sum)

if __name__ == "__main__":
    main()