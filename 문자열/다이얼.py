import sys
input = sys.stdin.readline

# 해시로 한번 풀어보자

a = list(input())
t = 0
for i in a:
    if 'A' <= i <= 'C':
        t += 3
    if 'D' <= i <= 'F':
        t += 4
    if 'G' <= i <= 'I':
        t += 5
    if 'J' <= i <= 'L':
        t += 6
    if 'M' <= i <= 'O':
        t += 7
    if 'P' <= i <= 'S':
        t += 8
    if 'T' <= i <= 'V':
        t += 9
    if 'W' <= i <= 'Z':
        t += 10
print(t)
