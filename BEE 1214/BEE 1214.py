n = int(input())
for _ in range(n):
    grades = input()
    grades = list(map(int , grades.split()))
    t = (grades.pop(0))
    average = sum(grades)/t
    count = 0
    for grade in grades:
        count += 1 if grade > average else 0
    print(f"{(count*100)/t:.3f}%")