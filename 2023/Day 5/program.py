import multiprocessing
import logging

f = open("input.txt", "r")
lines = f.read().splitlines()

def main():
    sources = [int(numbers) for numbers in lines[0][lines[0].index(":") + 2:].split(" ")]
    print("Sources finished!")

    pool = multiprocessing.Pool(12)

    destinations = pool.map(source_to_destination, range(314462259, 4114434577))

    pool.close()
    pool.join()

    #for j in range(314462259, 4114434577 + 1):
    #    contained = False
    #    print((j - 314462259) / (4114434577 + 1 - 314462259) * 100, "%")
    #    for i in range(0, len(sources), 2):
    #        if sources[i] < j and j < sources[i + 1]:
    #            contained = True
    #    if contained:
    #        destination = pool.map(source_to_destination, range(314462259, 4114434577 + 1))
    #        if destination < min:
    #            min = destination
    #
    min = 999999999999999
    for destination in destinations:
        if destination is int and destination < min:
            min = destination
    print(min)

def is_int(char):
    return 48 <= ord(str(char)) and ord(str(char)) <= 57

def source_to_destination(source):
    contained = False
    sources = [int(numbers) for numbers in lines[0][lines[0].index(":") + 2:].split(" ")]
    for i in range(0, len(sources), 2):
            if sources[i] < int(source) and int(source) < sources[i + 1]:
                contained = True

    if contained:
        blacklist = True
        for i in range(2, len(lines)):
            if len(lines[i]) > 0 and is_int(lines[i][0]):
                map = [int(numbers) for numbers in lines[i].split(" ")]
                if (map[1] <= source and source < map[1] + map[2]):
                    source = map[0] - map[1] + source
                    blacklist = True
            else:
                blacklist = False
        return source



if __name__ == "__main__":
    main()