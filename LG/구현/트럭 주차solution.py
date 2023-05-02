import sys
sys.stdin = open("트럭 주차.txt", "r")

a, b, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(3)]
maxtime = max(table[0][1], table[1][1], table[2][1])
parking = [0] * (maxtime-1)

print(maxtime)
print(parking)


for car in table:
    print(car[0], car[1])
    for i in range(car[0]-1, car[1]-1):
        parking[i] += 1

print(parking)
fee = 0

for i in parking:
    if i == 1:
        fee += a
    elif i == 2:
        fee += 2*b
    elif i == 3:
        fee += 3*c
print(fee)
