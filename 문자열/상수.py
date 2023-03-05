import sys
input = sys.stdin.readline


def rev(n):
    rn = 0
    while n > 0:
        rn *= 10
        rn += n % 10
        n = n//10
    return rn


a, b = map(int, input().split())
print(max(rev(a), rev(b)))
