string = input()

alpha = []
number = 0

for s in string:
  if s.isalpha():
    alpha.append(s)
  # 모든 숫자는 더한다
  else:
    number += int(s)

# 오름차순 정렬
alpha.sort()

print( "".join(alpha) + str(number))
