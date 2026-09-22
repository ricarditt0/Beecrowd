len = int(input())
values = []
marked = 0

for i in range(len):
    values.append(int(input()))

last = 0
for i in values:
    if (i != last) or (last == 0):
        marked += 1
    last = i
print(marked)
