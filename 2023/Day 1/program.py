NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def fix_line(line):
    first_found = False
    last_found = False
    for i in range(0, len(line)):
        if (48 <= ord(line[i]) and ord(line[i]) <= 57):
            break
        for j in range(len(NUMBERS)):
            if i == line.find(NUMBERS[j]):
                line = line.replace(NUMBERS[j], str(j + 1), 1)
                first_found = True
                break
        if first_found:
            break
    for i in range(len(line) - 1, -1, -1):
        if (48 <= ord(line[i]) and ord(line[i]) <= 57):
            break
        for j in range(len(NUMBERS)):
            if (48 <= ord(line[i]) and ord(line[i]) <= 57) or i == line.rfind(NUMBERS[j]):
                line = rreplace(line, NUMBERS[j], str(j + 1), 1)
                last_found = True
                break
        if last_found:
            break
    return line

def main():
    with open("input.txt", 'r') as i:
        lines = i.readlines()
    sum = 0
    for line in lines:
        original_line = line
        line = fix_line(line)
        number = 0
        for i in range(len(line)):
            if 48 <= ord(line[i]) and ord(line[i]) <= 57:
                number += int(line[i]) * 10
                break
        for i in range(len(line) - 1, -1, -1):
            if 48 <= ord(line[i]) and ord(line[i]) <= 57:
                number += int(line[i])
                break
        sum += number
        print(original_line, " --> ", line)
    print(sum)


if __name__ == "__main__":
    main()