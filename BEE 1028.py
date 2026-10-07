n = int(input())

for _ in range(n):

    a ,b = map(int, input().split())

    while b:
        a, b = b, a % b
    print(a)