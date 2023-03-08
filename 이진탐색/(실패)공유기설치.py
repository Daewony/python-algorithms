"""
예전에 마구간 문제랑 유사한 느낌이 든다

1. 아이디어
공유기 2개는 무조건 왼쪽 끝, 오른쪽 끝 2개이다
3개일때는 1/2랑 가장 가까운 숫자, abs 작은순서
4개일때는 1/3,2/3이랑 가장 가까운 숫자
5개일때는 1/4,2/4,3/4 가장 가까운 숫자

입력한 집들을 정렬한다
가까운 숫자를 이진 탐색으로 찾는다


1 2 4 8 9

1 3 8 9 10

2. 시간복잡도

3. 변수



"""


import sys
input = sys.stdin.readline

n, c = map(int, input().split())
h = []

for i in range(n):
    h.append(int(input()))
h.sort()
res = []
res.append(h[0])
res.append(h[n-1])


lt, rt = h[0], h[n-1]

for i in range(1, c-1):  # 1
    mid = (lt+rt)//2
    l = 0
    r = n-1
    while l <= r:
        m = (l+r)//2
        if h[mid] == mid:
