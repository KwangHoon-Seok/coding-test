total_stage = int(input())
stages = list(map(int, input().split()))
fail_rates = []

answer = []
count = 0 
total = len(stages)
for i in range(1, total_stage+1):
    count = stages.count(i)
    if total == 0:
        fail_rate = 0
    else:
        fail_rate = count / total
        total -= count
    fail_rates.append((i, fail_rate))

fail_rates.sort(key=lambda x: -x[1])

for fail_rate in fail_rates:
    answer.append(fail_rate[0])

print(answer)