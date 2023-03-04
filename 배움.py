import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bk = [i for i in range(n+1)]
# basket = [i+1 for i in range(n)]
# li = [_ for _ in range(1,n+1)]
# s = [*range(1,n+1)]

for i in range(m):
    a, b = map(int, input().split())
    for i in range(a, b+1):  # 1,2,3 -> 2,3
        bk[a], bk[b] = bk[a], bk[b]


for i in range(1, n+1):
    print(bk[i], end=" ")

# 역순에 취약하다

n, m = map(int, input().split())
arr = []
temp = 0
for i in range(1, n+1):
    arr.append(i)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for j in range((b-a)//2+1):  # 여기서 막힘
        temp = arr[a+j]
        arr[a+j] = arr[b-j]
        arr[b-j] = temp
print(*arr)
