"""
1. 아이디어
투 포인터를 활용
for문으로 K만큼 돌려, 첫 온도의 합을 구한다
처음의 인덱스와 마지막 인데스를 한칸씩 이동시킨다
움직일때마다 가장 큰값을 갱신한다


2. 시간복잡도
1e5
O(n2)안됨
o(n)으로 구성해보기 -> 투포인터, 이진탐색


3. 자료구조

온도 값들 = int[]
투 포인터: index = int
최대값 갱신: int


"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

total = 0  # 온도의 합
maxv = 0  # 최댓값

# K일 간의 온도의 합
for i in range(K):
    total += arr[i]

maxv = total

# 인덱스 한칸씩 이동후 최대값 갱신
for i in range(K, N):
    total += arr[i]
    total -= arr[i-K]
    maxv = max(maxv, total)

print(maxv)
