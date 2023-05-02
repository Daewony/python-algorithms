import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
ch = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(len(dx)):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and ch[ny][nx] == False:
                    rs += 1
                    ch[ny][nx] = True
                    q.append((ny, nx))
    return rs


cnt, maxa = 0, 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and ch[j][i] == False:
            ch[j][i] = True
            cnt += 1
            maxa = max(maxa, bfs(j, i))
print(cnt)
print(maxa)
