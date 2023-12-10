SYMBOLS = ['@', '#', '$', '%', '&', '*', '-', '+', '/']

def main():
    f = open("input.txt", 'r')
    lines = f.readlines()

    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            number_of_digits = 0
            if not is_int(lines[i][j]) or is_int(lines[i][j - 1]):
                continue

            # count digits
            number = 0
            index = j
            while is_int(lines[i][index]):
                number = number * 10 + int(lines[i][index])
                number_of_digits += 1
                index += 1

            # adjacent lines
            for k in range(-1, number_of_digits + 1):
                increment = 2
                if k == -1 or k == number_of_digits:
                    increment = 1
                for q in range(-1, 2, increment):
                    if (q == -1 and i == 0) or (q == 1 and i == len(lines) - 1) or (k == -1 and j == 0):
                        continue
                    if lines[i + q][j + k] == '.' and not is_int(lines[i + q][j + k]) and lines[i + q][j + k] != '\n':
                        print(i, ",", j + k, ",", number)
                        sum += number
                        break
    
    print(sum)

def is_int(char):
    return 48 <= ord(char) and ord(char) <= 57
            
if __name__ == "__main__":
    main()