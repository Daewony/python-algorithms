from collections import deque

n, k = map(int, input().split())
v = [0]*200001


# 왜 시간초과인지를 모르겠다


def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(v[now])
            return
        for next in (now-1, now+1, now*2):
            if 0 <= next <= 200000 and not v[next]:
                if next == now*2:
                    # 0초니까 맨앞으로 가야함(딜레이 없음)
                    q.appendleft(next)
                    v[next] = v[now]
                else:
                    q.append(next)
                    v[next] = v[now]+1


bfs()
