
def fat(x):
    if x == 0:
        return 1
    else:
        return x * (fat(x - 1)) 

try:
    while(True):
        x = input()
        x = x.strip().split(' ')
        n = fat(int(x[0]))
        m = fat(int(x[1]))
        print(n+m)


except EOFError:
    exit()