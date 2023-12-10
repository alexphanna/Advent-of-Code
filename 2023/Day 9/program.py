def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    sum = 0
    for line in lines:
        line = line.split(" ")[::-1]
        sum += next_value(line)
    print(sum)

def get_differences(numbers):
    differences = []
    for i in range(len(numbers) - 1):
        differences.append(int(numbers[i + 1]) - int(numbers[i]))
    return differences

def next_value(numbers):
    differences = get_differences(numbers)
    for i in differences:
        if i != 0:
            return next_value(differences) + int(numbers[len(numbers) - 1])
    return numbers[len(numbers) - 1]

if __name__ == "__main__":
    main()