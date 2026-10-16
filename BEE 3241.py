n = int(input())

for _ in range(n):
    problem = input()

    if problem == 'P=NP':
        print('skipped')

    else:
        a,b = problem.split('+')
        print(f'{int(a) + int(b)}')
