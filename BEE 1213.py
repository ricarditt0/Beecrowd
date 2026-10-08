while True:
    try:
        n = int(input())
    except EOFError:
        break

    count = 0
    rest = 0

    while True:
        rest = (rest * 10 + 1)%n
        count += 1

        if rest == 0:
            print(count)
            break