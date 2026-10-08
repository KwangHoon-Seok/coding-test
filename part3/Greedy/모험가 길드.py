
N = int(input())
people = list(map(int, input().split()))
people.sort()

groups = 0
count = 0
for scary in people:
    count += 1
    if scary == count:
        groups += 1
        count = 0

print(groups)

