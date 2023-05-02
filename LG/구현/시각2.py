hours = int(input())

count = 0
for h in range(hours+1):
    for m in range(60):
        for s in range(60):
            # 매 시각 확인
            if '3' in str(h)+str(m)+str(s):
                count += 1
print(count)
