import sys
sys.stdin = open("대표값2.txt", "r")

# arr = []
# for i in range(5):
#     arr.append(int(input()))

# ave = sum(arr)//len(arr)

# mid = max(arr)
# for i in arr:
#     if abs(i-ave) < mid:
#         mid = i

# print(ave)
# print(mid)

li = sorted([int(input()) for _ in range(5)])
print(sum(li)//5)
print(li[2])
