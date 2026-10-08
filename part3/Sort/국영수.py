# N명의 국어 - 영어 - 수학
N = int(input())
students = []
for _ in range(N):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])