def has_repeats(str):
    for i in range(0, len(str)):
        for j in range (i + 1, len(str)):
            if str[i] == str[j]:
                return True
    return False

f = open("input.txt", "r")
line = f.readline()

for i in range(0, len(line)):
    if not has_repeats(line[i:][:14]):
        print(i + 14)
        break
