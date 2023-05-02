"""
약수의 개수
약수

A = 8

진짜 약수 2,4 => 2
1,2,4,8 => 4

124 => 4

6
3 4 2 12 6 8
2 3 4 6 8 12


"""

N = int(input())
a = sorted(list(map(int, input().split())))
print(a[0]*a[-1])
