
def parity(x:int):
    if x <= 1:
        return "Not Prime"
    elif x <= 3:
        return "Prime"
    elif x % 2 == 0 or x % 3 == 0:
        return "Not Prime"
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return "Not Prime"
        i += 6
    return "Prime"     

N = int(input())
for c in range(0,N):
    number = int(input())
    print(f"{parity(number)}")