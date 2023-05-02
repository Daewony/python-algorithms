n = int(input())
plans = input().split()

# 상하좌우에 따른 이동방향
move_types = ['U', 'D', 'L', 'R']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 좌표
x, y = 1, 1

# 이동 계획에 따라 움직인다
for plan in plans:
    # 이동방향 확인
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동수행
    x, y = nx, ny

print(x, y)
