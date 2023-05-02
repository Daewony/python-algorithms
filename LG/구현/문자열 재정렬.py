"""

문자는 문짜끼리 숫자는 숫자끼리 정렬하기

"""
# 12분
# 설계를 하면서 풀자

import sys
sys.stdin = open("문자열 재정렬.txt", "r")
s = input()

apb = []
num = 0

print(ord('A'), ord('a'), ord('0'), ord('9'))


for i in s:
    if 48 <= ord(i) <= 57:
        # cn = ord(i)-ord('0')
        # num += cn
        num += int(i)
    else:
        apb.append(i)
apb.sort()
print(''.join(apb)+str(num))
