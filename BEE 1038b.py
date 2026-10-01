x,y = map(int, input().split())

total = 0
if x == 1:
    total = y * 4.0
elif x == 2:
    total = y * 4.5
elif x == 3:
    total = y * 5.0
elif x == 4:
    total = y * 2.0
elif x == 5:
    total = y * 1.5
print(f"Total: R$ {total:.2f}")