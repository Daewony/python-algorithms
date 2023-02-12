from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])  # 단어, 단계
    visited = [0] * len(words)  # 방문여부 확인(재방문 x)
    while q:
        word, cnt = q.popleft()
        # 종료 조건
        if word == target:
            answer = cnt
            break
        # 1개만 다른 단어 찾기
        for i in range(len(words)):
            diff = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    q.append([words[i], cnt+1])
                    visited[i] = 1
    return answer
