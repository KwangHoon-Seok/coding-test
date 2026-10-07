# from collections import deque

# def solution(prices):
#     answer = []
#     prices_q = deque(prices)
    
#     while prices_q:
#         first_price = prices_q.popleft()
#         count = 0
#         for i in range(len(prices_q)):
#             count += 1
#             if first_price > prices_q[i]:
#                 break
#         answer.append(count)
#     return answer

# arr = list(map(int, input().split()))
# print(solution(arr))

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []                      # 인덱스를 담음
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j       # j가 i에서 떨어짐
        stack.append(i)
    
    while stack:                    # 끝까지 안 떨어진 것들
        j = stack.pop()
        answer[j] = n - 1 - j
    
    return answer