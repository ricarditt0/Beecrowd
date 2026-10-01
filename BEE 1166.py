
tests = int(input())
for _ in range(tests):
    n = int(input())
    pags = [0] * n
    i = 1
    inceriu = True
    while inceriu:
        for j in range(n):
            soma = pags[j] + i
            if int(soma**0.5)**2 == soma or pags[j] == 0:
                pags[j] = i
                i += 1
                inceriu = True
                break
            if j == n - 1:
                inceriu = False
                break

        
    print(i - 1)
