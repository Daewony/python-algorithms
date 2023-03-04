"""
1. 아이디어
일곱 난쟁의 키의 합 = 100
2명은 사기꾼이다, 사기꾼을 거르기만 하면된다
조합 문제 같음
9명중 7명 = 9명중 2명

total = 9명 키의값

2중 for문으로 2명 뽑아서 합이 100인지 확인하기
맞으면 그 2명 빼고 배열에 입력하기

2. 시간복잡도


3. 변수
전체 키의 합: int
난쟁이들 키의 값들: int[]


"""

temp = []
find_seven = []

for i in range(9):
    temp.append(int(input()))

print(temp)

total = sum(temp)
tmp_two = 0
print("-------")
flag = False
for i in range(9):
    for j in range(i+1, 9):
        print(temp[i])
        print(temp[j])
        tmp_two = temp[i]+temp[j]
        res = total-tmp_two
        if res == 100:
            temp.remove(temp[i])
            temp.remove(temp[j])  # 왜 28을 없애???!??!?!?
            flag = True
            break
    if flag:
        break


print(sum(temp))
# for i in sorted(temp):
#     print(i)
