SUITS = [ "J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

ranks = [[], [], [], [], [], [], []]
def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    # Finds type
    for line in lines:
        line = line.split()
        number_of_suits = []
        for j in range(1, len(SUITS)):
            number_of_suit = 0
            for i in range(len(line[0])):
                if line[0][i] == SUITS[j]:
                    number_of_suit += 1
            if number_of_suit > 1:
                number_of_suits.append(number_of_suit)
        number_of_suits = sorted(number_of_suits)

        jokers = 0
        for i in range(len(line[0])):
            if "J" == line[0][i]:
                jokers += 1
        if len(number_of_suits) > 0:
            number_of_suits[len(number_of_suits) - 1] += jokers
        elif jokers == 5:
            number_of_suits.append(jokers)
        else:
            number_of_suits.append(jokers + 1)
        print(number_of_suits)

        if number_of_suits == [5]:
            ranks[6].append(line)
        elif number_of_suits == [4]:
            ranks[5].append(line)
        elif number_of_suits == [2, 3]:
            ranks[4].append(line)
        elif number_of_suits == [3]:
            ranks[3].append(line)
        elif number_of_suits == [2, 2]:
            ranks[2].append(line)
        elif number_of_suits == [2]:
            ranks[1].append(line)
        else:
            ranks[0].append(line)

    print(ranks)

    for rank in ranks:
        for i in range(0, len(rank)):
            for j in range(i + 1, len(rank)):
                if better_hand(rank[i][0], rank[j][0]):
                    temp = rank[i]
                    rank[i] = rank[j]
                    rank[j] = temp

    total_winnings = 0
    i = 1
    rank_number = 1
    for rank in ranks:
        print(rank_number)
        rank_number += 1
        for hand in rank:
            print(i, hand)
            total_winnings += i * int(hand[1])
            i += 1

    print(total_winnings)

def better_hand(hand1, hand2):
    i = 0
    while hand1[i] == hand2[i]:
        i += 1
    return SUITS.index(hand1[i]) > SUITS.index(hand2[i])


if __name__ == "__main__":
    main()