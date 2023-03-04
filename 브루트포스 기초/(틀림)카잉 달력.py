"""
1. 아이디어
while 문 안에서

x,y 증가 시킴 <=M,N
year +=1
x,y <=M,N일때까지 증가하고 그때의 year을 출력한다


2. 시간복잡도

3. 변수
테스트 횟수: int
M,N,x,y: int


"""
# 18분

from math import gcd


def lcm(x, y):
    return x*y//gcd(x, y)


T = int(input())
res = []
for i in range(T):
    M, N, x, y = map(int, input().split())
    tx, ty, year = 1, 1, 1
    end = lcm(M, N)
    # print(end)
    while year <= end:
        if tx == x and ty == y:
            res.append(year)
            break
        tx += 1
        ty += 1
        year += 1
        if tx == M:
            tx = 0
        if ty == N:
            ty = 0

    else:
        res.append(-1)

for i in res:
    print(i)
