notes = [100,50,20,10,5,2]
coins = [1.0,0.5,0.25,0.1,0.05,0.01]
result = [0,0,0,0,0,0,0]
value = float(input())
print("NOTAS:")
for i in range(0,6):
    result[i] = value//notes[i]
    print(f"{int(result[i])} nota(s) de R$ {notes[i]:.2f}")
    value = value%notes[i]
print("MOEDAS:")
value = value*100
for i in range(0,6):
    result[i] = value//(coins[i]*100)
    print(f"{int(result[i])} moeda(s) de R$ {coins[i]:.2f}")
    value = value%(coins[i]*100)