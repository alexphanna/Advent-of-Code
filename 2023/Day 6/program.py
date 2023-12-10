def main():
    times = 41777096
    distances = 249136211271011
    wins = 0

    # (times - seconds) * seconds

    for j in range(times + 1):
        print(j / 41777096 * 100)
        distance = (times - j) * j
        if distance > distances:
            wins += 1
    
    print(wins)
    product = 1
    for win in wins:
        product *= win
    print(product)


if __name__ == "__main__":
    main()