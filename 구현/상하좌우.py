"""
1. 아이디어
뱡향 리스트로
이동 계획서를 리스트에 담아서, for로 리스트를 하나씩 꺼내서
입력한 문제에 따라 이동시킨 후 (X,Y)를 출력한다

2. 시간 복잡도
n^2 = 100*100+4*100 = 10400 < 2천만

3. 자료구조
map: int[][]
dx, dy: int[]


if 맵을 넘치면 안된다

"""

# 27분 ->
# 처음에 map이라는 변수명을 써서 map()과 혼동이 되어 오류의 원인 + maps에 각 좌표를 넣을 필요가 없는데 넣어야 된다는 생각이 들음
# 방향 문자 switch 문으로 해결하면 좋을거같은데 기억이 어떻게 사용하는 건지 기억이 안났습니다
#


import sys
sys.stdin = open("상하좌우.txt", "r")
n = int(input())

move_list = input().split()  # list(map(str, input().split()))
move_type = ['R', 'D', 'L', 'U']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

y, x = 1, 1
print(move_list)


for plan in move_list:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        else:
            x, y = nx, ny

# for i in move_list:
#     if i == 'R':
#         nx = x + dx[0]
#         ny = y + dy[0]
#         if 1 <= nx <= n:
#             x = nx
#     elif i == 'D':
#         nx = x + dx[1]
#         ny = y + dy[1]
#         if 1 <= ny <= n:
#             y = ny
#     elif i == 'L':
#         nx = x + dx[2]
#         ny = y + dy[2]
#         if 1 <= nx <= n:
#             x = nx
#     elif i == 'U':
#         nx = x + dx[3]
#         ny = y + dy[3]
#         if 1 <= ny <= n:
#             y = ny

print(y, x)
