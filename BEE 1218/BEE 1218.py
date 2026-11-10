
j = 0
while True:
    try:
        n = int(input())
    except EOFError:
        break
    if j != 0:
        print()
    j += 1
    list_of_shoes = input().split()
    masculine = 0
    feminine = 0
    for i in range(0, len(list_of_shoes), 2):
        if int(list_of_shoes[i]) == n:
            masculine += 1 if list_of_shoes[i + 1] == "M" else 0
            feminine += 1 if list_of_shoes[i + 1] == "F" else 0
    print(f"Caso {j}:")
    print(f"Pares Iguais: {masculine + feminine}")
    print(f"F: {feminine}")
    print(f"M: {masculine}")
    