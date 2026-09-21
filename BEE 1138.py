while(True):
    digits = [0,0,0,0,0,0,0,0,0,0]
    x = input()
    if x == "0 0":
        break
    x = x.strip().split(' ')
    for num in range(int(x[0]),int(x[1])+1):
        for digit in str(num):
            digits[int(digit)] = digits[int(digit)] + 1

    for d in digits:
        print(f"{d} ",end='')
    print('')