# import sys
# input = sys.stdin.readline

while True:
    try:
        print(input())
    except EOFError:
        break

# for i in sys.stdin: # 계속 입력 받을려고해서 끝나지 않는다

#     if i == None:
#         break
#     print(i, end="")
