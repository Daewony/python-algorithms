"""
F층으로 이루어진 고층 건물에

스타트링크가 있는 곳의 위치는 G층

강호가 지금 있는 곳은 S층

엘리베이터를 타고 G층으로 이동

만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성

만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력

첫째 줄에 F, S, G, U, D
ex) 10층 현1층, 목표10층, 2번 위로, 1번 아래로 버튼

예제 1)왜 6인지 모르겠네
예제 2)D버튼 없으니
1,3,5,7,9,8,10

"""

# 런타임에러

import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
v = [0]*(f+1)

q = deque()
v[s] = 1
q.append(s)


while q:
    c = q.popleft()
    if c == g:
        print(v[c]-1)
        break
    for i in c+u, c-d:
        if not v[i] and 1 <= i <= f:  # 옥상위엔 층이 없어~
            v[i] = v[c]+1
            q.append(i)
else:
    print("use the stairs")
