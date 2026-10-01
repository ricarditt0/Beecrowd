x,y = map(int, input().split())

total = 0
match x:
    case 1:
        total = y * 4.0
    case 2:
        total = y * 4.5
    case 3:
        total = y * 5.0
    case 4:
        total = y * 2.0
    case 5:
        total = y * 1.5
print(f"Total: R$ {total:.2f}")