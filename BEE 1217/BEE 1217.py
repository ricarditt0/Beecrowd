n = int(input())
total_value = 0
total_weight = 0
for i in range(n):
    fruits_value = float(input())
    fruits = input().split()
    total_value += fruits_value
    total_weight += len(fruits)
    print(f"day {i+1}: {len(fruits)} kg")
print(f"{total_weight/n:.2f} kg by day")
print(f"R$ {total_value/n:.2f} by day")