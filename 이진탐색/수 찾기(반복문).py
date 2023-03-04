# 432ms

N = int(input())
A = list(map(int, input().split()))
K = int(input())
B = list(map(int, input().split()))

A.sort()


def binary_search(st, en, target):
    while st <= en:
        mid = (st+en)//2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            en = mid-1
        elif A[mid] < target:
            st = mid+1
    return 0


for x in B:
    print(binary_search(0, N-1, x))
