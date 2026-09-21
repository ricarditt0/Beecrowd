n1,n2,n3,n4 = [float(aux) for aux in input().split()]
media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print(f"Aluno aprovado.")
elif media < 5.0:
    print(f"Aluno reprovado.")
else:
    n1 = float(input())
    print(f"Aluno em exame.")
    media = (media + n1)/2
    print(f"Nota do exame: {n1}")
    if media >= 5.0:
        print(f"Aluno aprovado.")
    else:
        print(f"Aluno reprovado.")
    print(f"Media final: {media}")