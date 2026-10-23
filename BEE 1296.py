import math
while True:
    try:
        ma,mb,mc = map(float, input().split())
    except EOFError:
        break

    if (ma < mb + mc) and (mb < ma + mc) and (mc < ma + mb):
        s = (ma + mb + mc)/2
        a = (4/3)*math.sqrt(s*(s-ma)*(s-mb)*(s-mc))
        print(f'{a:.3f}')
    else:
        print(f'{-1:.3f}')