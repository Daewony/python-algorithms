n, k = map(int, input().split())
students = list(map(int, input().split()))
students.sort()
print(students[-k])
