n = int(input())
for _ in range(n):
    m,c = map(int, input().split())
    keys = list(map(int, input().split()))

    table = [None] * m
    for key in keys:
        position = key % m
        if table[position] == None:
            table[position] = [key]
        else:
            table[position].append(key)
    i = 0
    for lista in table:
        print(f'{i} -> ',end='')
        i += 1
        if lista != None:
            for key in lista:
                print(f'{key} -> ',end='')

        print(f'\\')
    if _ < n - 1:
        print()



    