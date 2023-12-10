def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    cards = [1] * 194
    
    for i in range(len(lines)):
        numbers_you_have = lines[i][lines[i].index(":") + 2:lines[i].index("|") - 1].replace("  ", " ").strip().split(" ")
        winning_numbers = lines[i][lines[i].index("|") + 2:].replace("  ", " ").split(" ")

        for j in range(cards[i]):
            number_of_wins = 0
            for number_you_have in numbers_you_have:
                for winning_number in winning_numbers:
                    if number_you_have == winning_number:
                        number_of_wins += 1
            for k in range(1, number_of_wins + 1):
                if i + k < len(cards):
                    cards[i + k] += 1

    print(cards)
    sum = 0
    for card in cards:
        sum += card
    print(sum)


if __name__ == "__main__":
    main()