import heapq

def solution(jobs):
    jobs.sort()                    # 요청 시각 순 정렬
    n = len(jobs)
    heap = []
    
    time = 0
    i = 0
    total = 0
    done = 0
    
    while done < n:
        # 현재 시각까지 도착한 것만 힙에 투입
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0], i))
            i += 1
        
        if heap:
            dur, req, _ = heapq.heappop(heap)
            time += dur
            total += time - req
            done += 1
        else:
            time = jobs[i][0]      # 할 일 없으면 다음 도착까지 점프
    
    return total // n