
def dfs(L):
    # 종료조건
    if L == r:
        print(result)
    else:
        for i in range(len(n)):
            if checklist[i] == 0:
                # 하나 뽑아서 넣기
                result[L] = n[i]
                # 뽑은 숫자 저장
                checklist[i] = 1
                dfs(L+1)
                # 백으로 돌아갈때 뽑은 숫자 반납
                checklist[i] = 0


n = [1, 2, 3, 4]
r = 2
result = [0]*r
checklist = [0]*len(n)

dfs(0)
