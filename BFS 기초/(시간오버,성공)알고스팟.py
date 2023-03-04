"""
1. 아이디어
maps로 지도 입력
방향키:상하좌우 int[] 배열
최소 몇개 부수어야하는지
bfs 최소이동 파악
이동경로중 벽 몇개있는지 파악
그 벽만큼 부수면 된다

2. 시간복잡도

3. 자료구조
이동 배열: int[], int[]
벽 부순 개수: int[]

"""
from collections import deque


n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(m)]
v = [[0]*n for _ in range(m)]
# print(n, m)
# for i in v:
#     print(i)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
#     print(i, j)

# 아니 왜 0이 나와???, if maps[ny][nx] == 1: 이 조건문 때문, 목표가 0이니까
# 예외 처리 잘하기 0일때, 1일때


def bfs(y, x):
    v[y][x] = 1
    q = deque()
    q.append([y, x])

    while q:
        cy, cx = q.popleft()
        if cy == m-1 and cx == n-1:
            print("부셔!", v[cy][cx]-1)
            return
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if 0 <= nx < n and 0 <= ny < m and not v[ny][nx]:
                if maps[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx]
                    q.appendleft([ny, nx])
                if maps[ny][nx] == 1:
                    v[ny][nx] = v[cy][cx]+1
                    q.append([ny, nx])


bfs(0, 0)
