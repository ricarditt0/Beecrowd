notes = [100,50,20,10,5,2,1]
result = [0,0,0,0,0,0,0]
value = int(input())
print(value)
for i in range(0,7):
    result[i] = value//notes[i]
    print(f"{result[i]} nota(s) de R$ {notes[i]},00")
    value = value%notes[i]