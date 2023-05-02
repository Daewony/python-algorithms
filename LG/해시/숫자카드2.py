import sys
input = sys.stdin.readline

# 인덱스로 접근하는 방법을 떠오름
# 그러나 음수가 있다는 것을 보고 잘못된 것임을 알아챔
# 이럴때 해시를 사용하는 건가? 싶다

n = int(input())
a = map(int, input().split())

# 1. hash에 num 개수 반영
hash = {}
for num in a:
    # 아무것도 없으면 0으로 해줘 + 1
    # 해시 자료구조가 num이라는 키가 있으면 갖다달라 + 1누적하겠다
    # 처음에 입력할때 키가 존재하지않아 파라미터 2개인 것이다
    # setdefault(a,b)
    # a라는 키가 존재하면 키가 갖고있는 값을 갖다달다
    # a라는 키가 존재하지 않으면 b를 반환해달라

    hash[num] = hash.setdefault(num, 0) + 1


m = int(input())
b = map(int, input().split())

for num in b:
    print(hash.setdefault(num, 0), end=" ")
