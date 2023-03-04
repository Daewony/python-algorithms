
from collections import deque


def bfs(s, e):
    # 큐 새성
    q = deque()
    v = [0]*200001

    # 초기데이터 삽입, v[] 방문초기화
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1  # 1로 시작함
        # 3방향, 범위내(0~200000), 미방문
        for n in (c-1, c+1, c*2):
            if 0 <= n <= 200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c]+1
    return -1


n, k = map(int, input().split())
res = bfs(n, k)
print(res)
