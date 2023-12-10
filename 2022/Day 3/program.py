def getPriority(char):
    if ord(char) >= 97:
        return ord(char) - 96
    elif ord(char) >= 65:
        return ord(char) - 38

# part 1
#
# def commonItem(rucksack):
#     for i in range(int(len(rucksack) / 2)):
#         for j in range(int(len(rucksack) / 2), int(len(rucksack))):
#             if rucksack[i] == rucksack[j]:
#                 return rucksack[i]

def commonItem(rucksack1, rucksack2, rucksack3):
    for item1 in rucksack1:
        for item2 in rucksack2:
            for item3 in rucksack3:
                if item1 == item2 and item2 == item3:
                    return item1


with open("input.txt", "r") as i:
    rucksacks = i.readlines()

total = 0
for i in range(0, len(rucksacks), 3):
    total += getPriority(commonItem(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]))

print(total)