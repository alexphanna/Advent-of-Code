import math
def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    queries = []
    steps = []

    for i in range(2, len(lines)):
        if lines[i][2] == "A":
            queries.append(lines[i][:3])
    
    for query in queries:
        step = 0
        i = 2
        while query[2] != "Z":
            if lines[i][:3] == query:
                if lines[0][step % len(lines[0])] == "L":
                    query = lines[i][7:10]
                elif lines[0][step % len(lines[0])] == "R":
                    query = lines[i][12:15]
                i = 2
                step += 1
            if i < len(lines) - 1:
                i += 1
            else:
                i = 2
        steps.append(step)
    print(math.lcm(int(steps[0]), int(steps[1]), int(steps[2]), int(steps[3]), int(steps[4]), int(steps[5])))

if __name__ == "__main__":
    main()