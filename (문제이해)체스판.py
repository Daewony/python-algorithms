"""
1. 아이디어
왼쪽 위의 색을 기준으로 체스판을 그린다

1째줄은 오른쪽만 비교
2째줄은 위 오른쪽 비교

다시 색칠한 부분이니깐
비교한 뒤 안맞은 부분은 수정, count +1 해준다

잘라내야한다! => 각 잘라낸 합들을 다 비교해야한다


2. 시간복잡도

3. 변수
board : int[][]
방향 비교: 북, 동
칠해야하는 개수: int
최솟값 : int

남동
  0 ~
  1 ~
  2 ~
  N ~
  이중 for
    0~N
      i~8+1<Mㄴ

"""

# 문제를 잘 이해하고 풀지 못했다.
# 나는 문제를 왼쪽 위 색깔을 기준으로 하면 되는줄 알았지만
# 문제는 왼쪽 색깔이 뭐든 적게 색칠하는 것을 찾아달라는 문제였다
# 그래서 wbwbwbwb 와 bwbwbwbw 를 대조하여 작은 값을 넣는 문제이다

n, m = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(n)]

for i in board:
    print(i)

# 동,북

# 칠해야할 개수
cnt = 0
# 그 중에서 최소
mini = 200000000

# 이동하는건 글러먹었다 GG
for l in range(n-8+1):
    for k in range(m-8+1):
        for j in range(l, 8+l):
            for i in range(k, 8+k):
                if j <= l and i < 7+k:
                    # 동 만 확인
                    print(*board[j], end=" -> ")
                    if board[j][i] == board[j][i+1]:
                        if board[j][i] == 'W':
                            board[j][i+1] = 'B'
                        elif board[j][i] == 'B':
                            board[j][i+1] = 'W'
                        cnt += 1
                p = 1
                for q in board:
                    if p:
                        print(q)
                        p = 0
                if j > l and i < 7+k:
                    # 북, 은 맞으니 현위치가 틀린거고 -> 무조건 맞지 않는다
                    if board[j][i] == board[j-1][i]:
                        if board[j-1][i] == 'W':
                            board[j][i] = 'B'
                        else:
                            board[j][i] = 'W'
                        cnt += 1
                    # 동, 은 틀리니 다음위치가 틀린 것
                    if board[j][i] == board[j][i+1]:
                        if board[j][i] == 'W':
                            board[j][i+1] = 'B'
                        else:
                            board[j][i+1] = 'W'
                        cnt += 1

        mini = min(mini, cnt)

print(mini)
