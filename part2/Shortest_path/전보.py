import heapq
INF = int(1e9)

node, edge, start = map(int, input().split())
graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)

# edge 정보 업데이트
for _ in range(edge):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y,Z))

def dijkstra(start):
    q = [] # priority q
    heapq.heappush(q, (0, start)) # dist, node
    distance[start] = 0
    while q:
        dist, current_node = heapq.heappop(q)
        if distance[current_node] < dist:
            continue
        for i in graph[current_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0 
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
