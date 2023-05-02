"""
1. 아이디어
탐색 알고리즘, 존재를 알아내는 프로그램

이진 탐색 활용(1e5라는 힌트, 10만)

    1 A배열을 정렬한다
    2 M배열에 대한 for문으로 하나씩 뽑아 search를 한다
    3 있으면 print(1)을 한뒤 return 한다
    4 없으면 print(0)


2. 시간복잡도
1e5
1e5
-1e9<int<1e^9
2^10 = 10^3


3. 자료구조
N,M : int
N에 대한 배열: int[]
M에 대한 배열: int[]

1 2 3 4 5

"""
# A[st]로 비교하고싶은데 범위를 넘었다는데 왜 그런지 모르겠음

# 508ms


N = int(input())
A = list(map(int, input().split()))
K = int(input())
B = list(map(int, input().split()))

A.sort()


def binary_search(st, en, target):
    if st > en:
        return 0
    mid = (st+en)//2
    if A[mid] == target:
        return 1
    elif A[mid] < target:
        return binary_search(mid+1, en, target)
    elif A[mid] > target:
        return binary_search(st, mid-1, target)


for target in B:
    print(binary_search(0, N-1, target))
