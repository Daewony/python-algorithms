"""
1. 아이디어
범위가 크다 -> 몇개인지 탐색 -> 이진탐색(10만개 넘음)

이진탐색을 활용, 투포인터도 가능할거같은데?

카드의 숫자를 정렬
이진탐색으로 nums의 하나하나의 값을 target으로하여 같은거 있을시 cnt 증가


2. 시간복잡도
-1e7 ~ 1e7
5e5


3. 자료구조
숫자 카드의 개수: int
카드의 숫자: int[]
정수의 개수: int
정수: int[]
그 정수값에 맞는 카드가 몇개 가지고 있는지: int[], 0으로 초기화


"""

# 시간 초과 ㅠㅠ

N = int(input())
card = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cnt = []

card.sort()
# print(card)

start, end = 0, N-1

# 중복을 어떻게 처리를 하냐가 관건인 문제
# mid가 중복 가운데 있다면


def binary_search(start, end, target):
    count = 0
    while start <= end:
        mid = (start+end)//2
        if card[mid] == target:
            while mid-1 >= 0 and card[mid-1] == target:
                mid = mid-1
            while mid+1 < N and card[mid+1] == target:
                count += 1
                mid = mid+1
            else:
                count += 1
        if card[mid] <= target:
            start = mid+1
        else:
            end = mid-1
    # print(count)
    return count


for x in nums:
    cnt.append(binary_search(start, end, x))

for i in cnt:
    print(i, end=" ")
