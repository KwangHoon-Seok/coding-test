import heapq

def solution(scoville, K):
    answer = 0
    # 힙 변수 선언
    scoville_heap = []
    for x in scoville:
        heapq.heappush(scoville_heap, x)
    while scoville_heap[0] < K:
        if len(scoville_heap) < 2:
            return -1
        first_low = heapq.heappop(scoville_heap)
        second_low = heapq.heappop(scoville_heap)
        if first_low >= K:
            break
        else:
            temp = first_low + (second_low * 2)
            heapq.heappush(scoville_heap, temp)
            answer += 1 
    return answer



arr = list(map(int, input().split()))
K = int(input())
print(solution(arr, K))