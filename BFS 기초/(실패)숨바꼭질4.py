"""
1. 아이디어
간던 곳을 반복하지 않기위해 다음방문 0인지 확인하기
dfs가 좋아보이나 가장빠른 길은 bfs로 찾아야한다

이동이 관건인 문제

2. 시간복잡도
1e5, 1e5
3. 자료구조


"""

from collections import deque


def bfs(s, e):
    v = [0]*200001
    v[s] = 1
    q = deque()
    q.append(s)

    while q:
        f = q.popleft()
        if f == e:
            return v[e]-1
        for i in (f-1, f+1, f*2):
            if 0 <= i <= 200000 and not v[i]:
                q.append(i)
                v[i] = v[f]+1


def move(now):
    data = []
    temp = now

    for _ in range(v[now]+1):
        data.append(temp)
        tmp = check[temp]
    print(' '.join(map(str, data[::-1])))


n, k = map(int, input().split())

res = bfs(n, k)
print(res)
dfs(n, k, res)
