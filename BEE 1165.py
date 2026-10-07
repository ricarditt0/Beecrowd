n = int(input())


for _ in range(n):
    num = int(input())
    primo = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            primo = False
            break
    if primo and num != 1 and num != 0:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
        