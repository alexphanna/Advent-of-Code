file = open("input.txt", "r")
lines = file.read().split("\n")

rules_array = list(line.split("|") for line in lines[:lines.index("")])
rules = {}
for rule in rules_array:
    if rule[0] not in rules:
        rules[rule[0]] = [rule[1]]
    else:
        rules[rule[0]].append(rule[1])

updates = list(line.split(",") for line in lines[lines.index("") + 1:])

def fix(update):
    i = 0
    while i < len(update):
        if update[i] not in rules:
            i += 1
            continue
        for j in range(len(rules[update[i]])):
            rule = rules[update[i]][j]
            if update[:i].count(rule) > 0:
                temp = update[i]
                update[i] = update[update.index(rule)]
                update[update.index(rule)] = temp
                i = 0
                break
        i += 1
    return update

part_one = 0
part_two = 0
for update in updates:
    correct = True
    for i in range(len(update)):
        if update[i] not in rules:
            continue
        for rule in rules[update[i]]:
            if update[:i].count(rule) > 0:
                correct = False
                break
        if not correct:
            break
    if correct:
        part_one += int(update[len(update) // 2])
    else:
        fixed = fix(update)
        part_two += int(fixed[len(fixed) // 2])


print(f"part 1: {part_one}")
print(f"part 2: {part_two}")
                

