def part_one():
    file = open("input.txt", "r")
    line = "".join(file.readlines())
    sum = 0
    for i in range(len(line)):
        if line[i:i+4] == "mul(":
            i += 4
            mul = line[i:line.index(")", i)].split(",")
            if len(mul) == 2 and mul[0].isdigit() and mul[1].isdigit():
                print(mul)
                sum += int(mul[0]) * int(mul[1])
    print(sum)

def part_two():
    file = open("input.txt", "r")
    line = "".join(file.readlines())
    mul_enabled = True
    sum = 0
    for i in range(len(line)):
        if line[i:i+4] == "do()":
            mul_enabled = True
            i += 4
        elif line[i:i+7] == "don't()":
            mul_enabled = False
            i += 6
        if mul_enabled and line[i:i+4] == "mul(":
            i += 4
            mul = line[i:line.index(")", i)].split(",")
            if len(mul) == 2 and mul[0].isdigit() and mul[1].isdigit():
                print(mul)
                sum += int(mul[0]) * int(mul[1])
    print(sum)


if __name__ == "__main__":
    part_two()