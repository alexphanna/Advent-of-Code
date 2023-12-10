import sys

with open("input.txt", 'r') as i:
    lines = i.readlines()

length = 3

maxes = [0] * length

total = 0
for i in lines:
    if i != "\n":
        total += int(i)
    else:
        for x in range(len(maxes)):
            if total > maxes[x]:
                maxes.insert(x, total)
                maxes.pop(len(maxes) - 1)
                break
        total = 0

sum = 0
for i in maxes:
    sum += i
print(sum)

        
