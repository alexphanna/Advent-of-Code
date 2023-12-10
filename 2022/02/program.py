import sys

def getScore(a, b):
    score = 0
    score += getOutcome(a, b)
    if b == "A":
        score += 1
    elif b == "B":
        score += 2
    elif b == "C":
        score += 3
    return score
    
def getOutcome(a, b):
    if ((b == "A" and a == "C") or (b == "B" and a == "A") or (b == "C" and a == "B")):
        return 6
    elif a == b:
        return 3
    else:
        return 0

with open("test.txt", "r") as i:
    rounds = i.readlines()

totalScore = 0
for round in rounds:
    you = ""
    if round[2] == "Y":
        you = round[0]
    elif round[2] == "Z":
        if round[0] == "A":
            you = "B"
        elif round[0] == "B":
            you = "C"
        elif round[0] == "C":
            you = "A"
    elif round[2] == "X":
        if round[0] == "A":
            you = "C"
        elif round[0] == "B":
            you = "A"
        elif round[0] == "C":
            you = "B"
    totalScore += getScore(round[0], you)

print(totalScore)
