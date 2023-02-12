"""
1. 아이디어
모든 경우의 수 => 완전탐색

초 일때 3이 있는 경우
분 일때 3이 있는 경우
시 일때 3이 있는 경우


2. 시간복잡도

3. 자료구조
hour: int
minutes: int
seconds: int

경우의 수, cnt: int

"""
# 25분 문제를 잘못봐서 5분 더 걸림

import sys
sys.stdin = open("시각.txt", "r")

cnt = 0

n = int(input())
for hour in range(n+1):
    for minutes in range(60):
        for seconds in range(60):
            tmp = str(hour) + str(minutes) + str(seconds)
            if tmp.find('3') != -1:
                print(tmp)
                cnt += 1
            # if '3' in str~~~

print(cnt)
