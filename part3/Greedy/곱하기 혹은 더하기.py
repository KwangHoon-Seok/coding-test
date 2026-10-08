# # 앞에서부터 하나씩 원소를 빼면서 더할지 곱할지 정하면됨
# from collections import deque
# arr = list(input())
# arr_queue = deque(arr)

# total = 0

# while len(arr_queue) > 1:
#     value_1 = int(arr_queue.popleft())
#     value_2 = int(arr_queue.popleft())

#     value_sum = value_1 + value_2 
#     value_mul = value_1 * value_2

#     if value_sum > value_mul:
#         total = value_sum
#         arr_queue.appendleft(value_sum)
#     else:
#         total = value_mul
#         arr_queue.appendleft(value_mul)
# print(total)

s = input()

# 첫 번째 문자를 숫자로 변경하여 초기화
result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    # 두 수 중 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행 (더하기는 곱하기 1의 특성과 같다)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)