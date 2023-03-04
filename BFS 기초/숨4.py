from collections import deque

# 전체크기 100000이지만 *2 때문에 200000으로 넓힘
# 최단이동을 어떻게 하는지 출력 - move함수 이용


n, k = map(int, input().split())
v = [0]*200001
c = [0]*200001

# 수빈 이동경로 확인


def move(now):
    # 경로 탐색 시작
    data = []
    # 역으로 경롤 찾기
    temp = now
    # print(v[now])
    # 걸리는 시간만큼 반복
    # print("v[now]:", v[now])
    for _ in range(v[now]):
        data.append(temp)
        temp = c[temp]
    print(' '.join(map(str, data[::-1])))


def bfs(s, e):

    v[s] = 1
    q = deque()
    q.append(s)

    while q:
        f = q.popleft()
        if f == e:
            print(v[e]-1)
            move(e)
            return
        for next in (f-1, f+1, f*2):
            if 0 <= next <= 200000 and not v[next]:
                q.append(next)
                v[next] = v[f]+1
                c[next] = f
                # print(c[next])


bfs(n, k)
