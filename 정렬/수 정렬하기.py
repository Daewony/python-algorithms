import sys
sys.stdin = open("수 정렬하기.txt", "r")

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)
