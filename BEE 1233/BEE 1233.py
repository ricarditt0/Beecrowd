def factoring(n:int)->list:
    fatores = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            fatores.append(i)
        while n%i == 0:
            n //=i 

        if n > 1:
            fatores.append(n)

    return fatores



while True:
    try: 
        n = int(input())
    except EOFError:
        break

    original = n

    for p in factoring(n):
        original -= original//p

    print(original//2)

    