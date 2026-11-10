
sets = [
    [(0,0),(0,1),(0,2)], # linhas
    [(1,0),(1,1),(1,2)], # 
    [(2,0),(2,1),(2,2)], # 
    [(0,0),(1,0),(2,0)], # colunas
    [(0,1),(1,1),(2,1)], #
    [(0,2),(1,2),(2,2)], #
    [(0,0),(1,1),(2,2)], # diagonais
    [(0,1),(1,2),(2,0)], #
    [(0,2),(1,0),(2,1)], #
    [(0,2),(1,1),(2,0)], # diagonal secundaria
    [(0,1),(1,0),(2,2)], #
    [(0,0),(1,2),(2,1)] #

]

def backtracking(matriz, index):
    if index == len(sets):
        return 0

    patern = sets[index]

    # maior quantidade de vezes que o pardão pode ser retirado da matriz
    k = min(
        matriz[patern[0][0]][patern[0][1]],
        matriz[patern[1][0]][patern[1][1]],
        matriz[patern[2][0]][patern[2][1]]
    )

    best = 0

    for i in range(k,-1,-1):

        # remover o padrão da matriz
        matriz[patern[0][0]][patern[0][1]] -= i
        matriz[patern[1][0]][patern[1][1]] -= i
        matriz[patern[2][0]][patern[2][1]] -= i

        # chamada recursiva para o proximo padrão
        result = i + backtracking(matriz, index + 1)

        # atualizar o melhor resuldado
        best = max(best,result)

        # restaurar a matriz
        matriz[patern[0][0]][patern[0][1]] += i
        matriz[patern[1][0]][patern[1][1]] += i
        matriz[patern[2][0]][patern[2][1]] += i

    return best

n = int(input())
while n:
    # Matriz 3x3
    #           1 2 3
    # circulo   1
    # quadrado    1
    # triangulo     1
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

   
    for i in range(n):

        quantidade, forma = input().split()
        linha = 0
        coluna = 0

        match forma:
            case "circulo" | "circulos":
                linha = 0
            case "quadrado" | "quadrados":
                linha = 1
            case "triangulo" | "triangulos":
                linha = 2

        match quantidade:
            case "um":
                coluna = 0
            case "dois":
                coluna = 1
            case "tres":
                coluna = 2
        matriz[linha][coluna] += 1

    repetidos = 0
    for i in range(3):
        for j in range(3):
            while matriz[i][j] >= 3:
                matriz[i][j] -= 3
                repetidos += 1

    number_of_set = backtracking(matriz, 0) + repetidos


    n = int(input())
    print(number_of_set)     
        
