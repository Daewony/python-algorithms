"""
1. 아이디어
상하좌우 움직일때 주사위 위치변화 알기
바닥면이 0일때 주사위 바닥면 쓰여있는 수가 칸에 복사
0이 아닌 경우 칸에 쓰여 있는 구 주사위 바닥면으로 복사, 칸에 쓰여있는 수 0


2. 시간복잡도

3. 변수
지도 세로,지도 가로, 명령의 개수: int
주사위 좌표: int[]


"""
"""

실패 원인:
    문제를 이해하는데 19분 걸림
    일일이 손으로 구상함
    단순반복 동작이니, 상하좌우 주사위가 어떻게 변화하고 그에 대한 대응을 하면 될것인데 변화를 알고자 손으로 먼저 푸니 30분 초과
    아이디어의 중요성



"""
n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
print("######")

for i in range(k):
    # 동
    if cmd[i] == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
        nx = x + dx[0]
        ny = y + dy[0]
    # 서
    if cmd[i] == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
        nx = x + dx[1]
        ny = y + dy[1]
    # 북
    if cmd[i] == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
        nx = x + dx[2]
        ny = y + dy[2]
    # 남
    if cmd[i] == 4:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]
        nx = x + dx[3]
        ny = y + dy[3]

    if 0 <= nx < m and 0 <= ny < n:
        if board[ny][nx] == 0:
            board[ny][nx] = dice[6]
        else:
            dice[6] = board[ny][nx]
            board[ny][nx] = 0  # 이걸 안해줬네
        x = nx
        y = ny
        print(dice[1])
