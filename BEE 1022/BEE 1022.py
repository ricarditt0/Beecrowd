def mdc(a:int, b:int) -> int :
    while b != 0:
        a, b = b, a % b
    return int(a)

n = int(input())
for _ in range(n):
    expression = input().split()
    n1 = int(expression[0])
    d1 = int(expression[2])
    n2 = int(expression[4])
    d2 = int(expression[6])
    nr = 0
    dr = 0
    match expression[3]:
        case "-":
            nr = (n1 * d2) - (n2 * d1)
            dr = d1 * d2
        case "+":
            nr = (n1 * d2) + (n2 * d1)
            dr = d1 * d2
        case "*":
            nr = n1 * n2
            dr = d1 * d2
        case "/":
            nr = n1 * d2
            dr = n2 * d1
    print(f"{nr}/{dr} = {int(nr/mdc(nr,dr))}/{int(dr/mdc(nr,dr))}")