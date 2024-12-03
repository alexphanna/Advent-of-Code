def is_safe(numbers):
    is_increasing = numbers[0] < numbers[1]
    for i in range(len(numbers) - 1):
        if (is_increasing and numbers[i] > numbers[i + 1]) or (not is_increasing and numbers[i] < numbers[i + 1]) or 1 > abs(numbers[i] - numbers[i + 1]) or 3 < abs(numbers[i] - numbers[i + 1]):
            return False
    return True

def part_two():
    file = open("input.txt", "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            print(line)
            sum += 1
        else:
            for i in range(len(numbers)):
                if (is_safe(numbers[0:i] + numbers[i + 1:len(numbers)])):
                    print(line)
                    sum += 1
                    break

    print(sum)

def part_one():
    file = open("input.txt", "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        if is_safe(list(map(int, line.split()))):
            sum += 1
    print(sum)

if __name__ == "__main__":
    part_two()