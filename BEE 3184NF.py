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

def dfs(i,j):
    if visited[i][j]:
        return 0

    visited[i][j] = True

    # se for ouro pega
    gold = 1 if board[i][j] == "G" else 0

    #verifica se tem armadilha proxima
    for di,dj in directoins:
        ni = i + di
        nj = j + dj

        if board[ni][nj] == "T":
            return gold

    #tenta avançar 
    for di,dj in directoins:
        ni = i + di
        nj = j + dj

        if board[ni][nj] != "T" and board[ni][nj] != "#" and not visited[ni][nj]:
            gold += dfs(ni,nj)
        
    return gold
        

print(dfs(player_posy,player_posx))