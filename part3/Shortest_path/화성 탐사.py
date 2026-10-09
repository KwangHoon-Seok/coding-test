import heapq
test_case = int(input())
INF = 1e9

result = []

def dikjstra(map, distance):
    global result
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x = 0
    y = 0
    # 다익스트라 알고리즘 구현 
    q = []
    heapq.heappush(q, (map[x][y], x, y)) # 에너지 소모량 - x - y
    distance[x][y] = map[x][y]
    while q: 
        energy, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or  nx >= N or 0 > ny or  ny >= N:
                continue
            cost = map[nx][ny] + energy
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    result.append(distance[N-1][N-1])


for _ in range(test_case):
    maps = []
    N = int(input())
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    #최단경로 표
    distance = [[INF] * (N) for _ in range(N)]

    dikjstra(maps, distance)

print(result)