"""
1. 아이디어


2. 시간복잡도

n = 10^5
k = 10^5
10^10 = 100억 > 2억
n^2 이하의 복잡도로 풀어야한다

3. 자료구조


"""
n, k = 10, 2
a = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
# n, k = 10, 5
# a = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]

# n,k = map(int,input().split())
# a = list(map(int,input().split()))

# n-k+1 번 비교함
# sum = 0
# maxi = 0
# for i in range(n-k+1):
#     sum = a[i]
#     for j in range(i+1, i+k):
#         sum += a[j]
#     maxi = max(maxi, sum)
# print(maxi)

sum = 0
end = 0
maxi = 0

for start in range(n-k+1):
    print(start, end)
    while end-start+1 <= k and end < n:
        sum += a[end]
        end += 1
    # print(sum)
    maxi = max(maxi, sum)
    sum -= a[start]

print(maxi)
