"""
1. 아이디어
각 변수마다 범위가 있는데 주어진 수는 어떤 년도 일까?

15의 배수, 28의 배수, 19의 배수

큰 수 부터 보기

    1) 지구,태양,달 값이 같은지
    2) 태양, 달 값이 같으니
    3) 다 다른지


2. 시간복잡도

3. 변수
지구: int
태양: int
달: int


"""

e, s, m = map(int, input().split())
each = [1, 1, 1]
year = 1

while True:
    if each[0] == e and each[1] == s and each[2] == m:
        print(year)
        break
    for i in range(len(each)):
        each[i] += 1
    if each[0] > 15:
        each[0] = 1
    if each[1] > 28:
        each[1] = 1
    if each[2] > 19:
        each[2] = 1
    year += 1
    # print(year)
