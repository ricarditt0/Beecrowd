import math
try:
    x = input()
    while(x.isprintable()):
        x = x.strip().split(' ')
        R1 = int(x[0])
        X1 = int(x[1])
        Y1 = int(x[2])
        R2 = int(x[3])
        X2 = int(x[4])
        Y2 = int(x[5])

        dist = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
        if dist + R2 <= R1:
            print("RICO")
        else:
            print("MORTO")
        x = input()

except EOFError:
    exit()
    