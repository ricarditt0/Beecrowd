n = int(input())
for i in range(n):
    num,base = input().split()
    match base:
        case 'bin':
            print(f'Case {i+1}:\n{int(num,2)} dec\n{hex(int(num,2))[2::]} hex\n')
        case 'dec':
            print(f'Case {i+1}:\n{hex(int(num))[2::]} hex\n{bin(int(num))[2::]} bin\n')
        case 'hex':
            print(f'Case {i+1}:\n{int(num,16)} dec\n{bin(int(num,16))[2::]} bin\n')