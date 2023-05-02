"""
1. 아이디어
'건' '순' 이렇게 그래프로 나뉘어 가장 빠르게 도착하기 위한 알고리즘은 BFS이다

큐로 입력,
목적지에 도달했을때 cnt 출력

2. 시간복잡도
1e5, 1e5
bfs -> o(N^2) = 1e10? 100억?
가능한가?


3. 자료구조
수빈이 위치: int
동생 위치: int
위치 이동 입력: queue
방문: int[]
이동 시간: int

"""
from collections import deque

n, k = map(int, input().split())
visited = [0]*200001

# 방문으로 중복여부를 없애야할 거같은데
# 방문을 이상하게 넣어서 그런지 런타임 에러가된다


def bfs(s, d):
    # 방문
    visited[s] = 1
    q = deque()
    q.append([s, d])
    while q:

        x, d = q.popleft()
        # print(x, d)
        visited[x] = 1
        if x == k:
            return d
        else:
            if 0 <= 2*x <= 200000 and
            q.append([x+1, d+1])
            q.append([x-1, d+1])
            q.append([2*x, d+1])


print(bfs(n, 0))


# print("seconds:", bfs(n, 0))
