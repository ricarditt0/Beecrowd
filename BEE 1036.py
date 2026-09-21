import math

a,b,c = [float(aux) for aux in input().split()]
delta = b**2 - 4*a*c
if a == 0 or delta < 0:
    print(f"Impossivel calcular")
else:    
    r1 = ((-b) + math.sqrt(delta))/(2*a)
    r2 = ((-b) - math.sqrt(delta))/(2*a)
    print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
