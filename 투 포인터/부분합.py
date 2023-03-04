n, s = 10, 15
data = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

# n,s = map(int,input().split())
# data = list(map(int,input().split()))


res = 2148000000
sum = 0
r = 0

for l in range(n):
    while sum < s and r < n:
        sum += data[r]
        r += 1
        print(l, r, sum)
    if sum >= s and res > r-l:
        res = r-l
    print(res)
    sum -= data[l]

print(res)
