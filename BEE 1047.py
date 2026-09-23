hi, mi, hf, mf = map(int, input().split())
fim = (hf * 60 + mf)
inicio = (hi * 60 + mi)

if fim < inicio:
    fim += 24*60

duracao = fim - inicio

print(f'O JOGO DUROU {duracao // 60} HORA(S) E {duracao % 60} MINUTO(S)')