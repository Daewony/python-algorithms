import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input().rstrip())

b = set()
for i in range(m):
    b.add(input().rstrip())

res = sorted(list(a & b))
# print(len(res))
# for i in res:
#     print(i)
print(len(res), *res, sep="\n")


# hash = {}
# for i in range(n):
#     a = input()
#     hash[a] = hash.setdefault(a, 0) + 1

# for i in range(m):
#     a = input()
#     hash[a] = hash.setdefault(a, 0) + 1


# hash.sort()
# for i in hash:
#     if hash[i] >= 2:
#         print(i.rstrip())
