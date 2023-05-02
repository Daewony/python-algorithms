"""
1. 아이디어
적정치의 높이를 빨리 찾아야한다(양이 큼으로)
작은 나무 + 큰나무 // 2 하면서
모든 나무들을 다 잘라서 구한다

구하려는 나무 M미터보다 크면 높이를 줄이고
M미터보다 작으면 높이를 올려
적정한 높이의 최대값을 구한다

이진탐색 빨로는 저 용량의 시간복잡도를 해결할 수 있을까?


2. 시간복잡도

1e6, 1백만
2e9, 20억

3. 자료구조
나무의 수 :int
가져가려고 하는 나무의 길이: int
나무들의 높이들: int[]
자른 나무들의 합: int
최댓값: int


"""

N, M = map(int, input().split())
trees_h = list(map(int, input().split()))

best_h = 0


def binary_search(start, end, target, best_h):
    while start <= end:
        mid = (start+end)//2
        total = 0  # 자른 나무들의 합
        for i in trees_h:
            if i > mid:
                total += (i-mid)
        if total == M:
            return mid  # 이게 최대일거라고 보장은 없잖아?
        # 그래서 틀림 .i.i. 같은 나무라면 중간에 잘라도 mid값이랑 같지만 최대 높이는 아니게된다
        elif total < M:
            end = mid - 1  # 반대로한건가? 이미지를 떠올리자
        elif total > M:
            best_h = max(best_h, mid)
            start = mid+1
    return best_h


# 1 or 0부터 시작 안했다고 틀림, 왜일까?
print(binary_search(min(trees_h), max(trees_h), M, best_h))
