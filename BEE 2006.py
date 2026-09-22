resposta = int(input())
jurados = [int(i) for i in input().split()]
acertos = 0
for i in jurados:
    if i == resposta:
        acertos += 1
print(acertos)