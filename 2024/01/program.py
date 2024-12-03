def part1():
    with open("input.txt", 'r') as i:
        lines = i.readlines()
    firstArray = []
    secondArray = []
    for line in lines:
        firstArray.append(int(line.split()[0]))
        secondArray.append(int(line.split()[1]))
    firstArray.sort()
    secondArray.sort()
    distance = 0
    for i in range(0, len(firstArray)):
        distance += abs(firstArray[i] - secondArray[i])
    print(distance)

def count(array, target):
    count = 0
    for number in array:
        if number == target:
            count += 1
    return count

def part2():
    with open("input.txt", 'r') as i:
        lines = i.readlines()
    firstArray = []
    secondArray = []
    for line in lines:
        firstArray.append(int(line.split()[0]))
        secondArray.append(int(line.split()[1]))
    sum = 0
    for i in range(0, len(firstArray)):
        sum += firstArray[i] * count(secondArray, firstArray[i])
    print(sum)


if __name__ == "__main__":
    part2()