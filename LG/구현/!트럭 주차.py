"""
트럭 3대 -> 트럭 주차 총 비용
트럭수 만큼 할인



"""

import sys
sys.stdin = open("트럭 주차.txt", "r")

a, b, c = map(int, input().split())
s = min(a, b, c)
e = max(a, b, c)

car = []


# == for _ in range(3):
#     tmp = list(map(int, input().split()))
#     car.append(tmp)

print(car)


car_num = [0]*3
sum = 0

for i in range(s, e+1):  # 1~6시
    for k in range(3):
        if car[k][0] <= i and car[k][1] > i:

        if car[k][1] < i:
            car_num -= 1
    print(i, car_num)
    if car_num == 1:
        sum = sum + a
    elif car_num == 2:
        sum = sum + b*2
    elif car_num == 3:
        sum = sum + c*3
print(sum)
