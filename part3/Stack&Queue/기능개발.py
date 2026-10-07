from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses_deque = deque(progresses)
    speeds_deque = deque(speeds)
    while progresses_deque:
        # 각 원소별로 더하기
        for i in range(len(progresses_deque)):
            progresses_deque[i] += speeds_deque[i]
        count = 0
        while progresses_deque and progresses_deque[0] >= 100:
            progresses_deque.popleft()
            speeds_deque.popleft()
            count += 1
        if count > 0:
            answer.append(count)

    return answer

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solution(A,B))