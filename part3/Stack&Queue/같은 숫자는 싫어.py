# 스택으로 접근해서 array를 다 넣은 다음에 하나씩 뽑으면서 같은 거면 지우기
def solution(arr):
    answer = []
    temp = arr.pop()
    answer.append(temp)
    for _ in range(len(arr)):
        A = arr.pop()
        if temp == A:
            continue
        else:
            temp = A
            answer.append(A)

    answer.reverse()
    return answer

# def solution_A(arr):
#     answer = []
#     for x in arr:
#         if not answer or answer[-1] != x:
#             answer.append(x)

arr = list(map(int, input().split()))

print(solution(arr))