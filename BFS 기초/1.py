"""
1. 아이디어
가장빠른 시간 몇초후
2. 시간복잡도
1e5
3. 자료구조
큐

"""

from collections import deque


def bfs(s, e):
    v = [0]*200001
    v[s] = 1

    q = deque()
    q.append(s)
    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1
        for i in (c-1, c+1, c*2):
            if 0 <= i <= 200000 and v[i] == 0:
                q.append(i)
                v[i] = v[c]+1
    return -1


n, k = map(int, input().split())
print(bfs(n, k))
