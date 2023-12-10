with open("input.txt", "r") as i:
    assignments = i.read().splitlines()

# part 1

def contains(a1, a2, b1, b2):
    if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
        return True
    return False

# part 2

def overlaps(a1, a2, b1, b2):
    if (a1 >= b1 and a1 <= b2) or (a2 >= b1 and a2 <= b2) or contains(a1, a2, b1, b2):
        return True
    return False

total = 0
for assignment in assignments:
    numbers = assignment.replace(",", "-").split("-")
    if overlaps(int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])):
        print(numbers)
        total += 1

print(total)