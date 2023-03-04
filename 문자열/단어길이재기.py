import sys
import re
input = sys.stdin.readline

s = input()
# apb = 'abcdefghijklmnopqrstuvwxyz'
apb = list(range(ord('a'), ord('z')+1))

for i in apb:
    print(s.find(chr(i)), end=' ')


# for i in apb:
#     if i in s:
#         print(s.index(i), end=' ')
#     else:
#         print(-1, end=' ')


# s = list(map(str, input().strip()))
# print(ord('a'), ord('z'))
# try:
#     for i in range(ord('a'), ord('z')+1):
#         print(s.index(chr(i)), end=" ")
# except:
#     print(-1, end=" ")
# for i in range(ord('a'),ord('z')+1):
