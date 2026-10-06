def calculateMex(Set):
    Mex = 0

    while (Mex in Set):
        Mex += 1

    return (Mex)

def calculateGrundy(max_N = 10000):
    grundy = [0] * (max_N + 1)
    for n in range(1, max_N + 1):
        values = set()
        for i in range(1, n + 1):
            values.add(grundy[max(0, i - 3)] ^ grundy[max(0, n - i - 2)])
        grundy[n] = calculateMex(values)
    return grundy

grundy = calculateGrundy()
lista = str(grundy).replace('[', '').replace(']', '').replace(' ', '')
print(lista)
