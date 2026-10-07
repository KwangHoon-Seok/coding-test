from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    count = 0
    while q:
        cur = q.popleft()
        if any(cur[1] < other[1] for other in q):
            q.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count