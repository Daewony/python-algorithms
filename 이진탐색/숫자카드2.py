n = int(input())
d = [0]*20000001
for i in map(int, input().split()):
    d[i] += 1
m = int(input())
for i in map(int, input().split()):
    print(d[i], end=' ')

# 플레 5, 골드 1 목표
