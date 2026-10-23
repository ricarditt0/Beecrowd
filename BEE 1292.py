import math
while True:
    try:
        f = float(input())
    except EOFError:
        break
    lado = f*(math.sin(math.radians(108))/math.sin(math.radians(63)))

    print(f'{lado:.10f}')

