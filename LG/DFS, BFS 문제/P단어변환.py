from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()
        print("x, cnt:", x, cnt)
        if x == target:
            return cnt

        for i in range(len(words)):
            diff = 0
            word = words[i]
            print("word:", word)
            for j in range(len(x)):
                print(x[j], word[j])
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])
    return 0


solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
