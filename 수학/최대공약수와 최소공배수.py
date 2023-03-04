"""

1e4 *1e4 = 1e8 = 1억
2*3*3 = 18
3*2*2*2 = 24

   24 18


"""

A, B = map(int, input().split())
a, b = A, B
while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)

# lcm
print(A*B//a)

# max_same_num = 0
# min_mul_num = 0

# for i in range(2, end+1):
#     if a % i == 0 and b % i == 0:
#         max_same_num = i
# print(max_same_num)

# min_mul_num = max_same_num*(a//max_same_num)*(b//max_same_num)
# print(min_mul_num)
