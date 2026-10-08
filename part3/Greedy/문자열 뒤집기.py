numbers = input()

first_value = numbers[0]
# 0로 뒤집을 경우
count_0 = 0
flag_0 = False
for i in range(len(numbers)):
    if flag_0 == False and numbers[i] == '1':
        flag_0 = True
        count_0 += 1
    elif numbers[i] == '0':
        flag_0 = False
    
# 1로 뒤집을 경우
count_1 = 0
flag_1 = False
for i in range(len(numbers)):
    if flag_1 == False and numbers[i] == '0':
        flag_1 = True
        count_1 += 1
    elif numbers[i] == '1':
        flag_1 = False

result = min(count_0, count_1)

print(result)

# s = input()

# count_0 = 0 # 전체를 0으로 만드는 횟수 (1 덩어리 수)
# count_1 = 0 # 전체를 1로 만드는 횟수 (0 덩어리 수)

# # 첫 번째 원소 처리
# if s[0] == '1':
#     count_0 += 1
# else:
#     count_1 += 1

# # 두 번째 원소부터 이전 원소와 달라지는 지점(경계)을 확인
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         # 다음 숫자가 1로 바뀐다면 -> 새로운 '1 덩어리' 시작
#         if s[i + 1] == '1':
#             count_0 += 1
#         # 다음 숫자가 0으로 바뀐다면 -> 새로운 '0 덩어리' 시작
#         else:
#             count_1 += 1

# print(min(count_0, count_1))