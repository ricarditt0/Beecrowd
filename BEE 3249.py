n = int(input())
wins = 0
for _ in range(n):
    battle = input()
    if battle.find('CD') == -1:
        wins += 1
print(wins)