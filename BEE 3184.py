w,h = map(int,input().split())

board = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    line = str(input())
    board[i] = line

player_posx = 0
player_posy = 0

visited = [[False] * w for _ in range(h)]

for i in range(1,h-1):
    if board[i].find('P') != -1:
        player_posx = board[i].index('P')
        player_posy = i

directoins = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]

fronteira = [(player_posy,player_posx)]
gold = 0
while fronteira:
    i,j = fronteira.pop()

    if visited[i][j]:
        continue

    visited[i][j] = True

    if board[i][j] == "G":
        gold += 1

    near_trap = False

    for di,dj in directoins:
        ni = i + di
        nj = j + dj
        if board[ni][nj] == "T":
            near_trap = True
            break

    if near_trap:
        continue

    for di,dj in directoins:
        ni = i + di
        nj = j + dj
        if board[ni][nj] != "T" and board[ni][nj] != "#" and not visited[ni][nj]:
            fronteira.append((ni,nj))
        
print(gold)