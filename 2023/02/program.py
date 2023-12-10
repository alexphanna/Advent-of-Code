def main():
    with open("input.txt", 'r') as i:
        lines = i.readlines()
    sum = 0
    for line in lines:
        colors = [0, 0, 0]
        id = int(line.split(" ")[1].replace(":", ""))
        i = line.index(":") + 2
        while i < len(line):
            if 48 <= ord(line[i]) and ord(line[i]) <= 57:
                number = int(line[i])
                if 48 <= ord(line[i + 1]) and ord(line[i + 1]) <= 57:
                    number = number * 10 + int(line[i + 1])
                    i += 1
                if line[i + 2] == "r" and colors[0] < number:
                    colors[0] = number
                elif line[i + 2] == "g" and colors[1] < number:
                    colors[1] = number
                elif line[i + 2] == "b" and colors[2] < number:
                    colors[2] = number
            i += 1
        sum += colors[0] * colors[1] * colors[2]
    print(sum)
    


if __name__ == "__main__":
    main()