# ------다익스트라 version-------
# import heapq
# INF = int(1e9)

# node, edge = map(int, input().split())
# graph = [[] for i in range(node + 1)]

# distance = [INF] * (node + 1)

# def initialization():
#     distance = [INF] * (node + 1)

# # edge 정보 -> 간선 비용은 항상 1
# for _ in range(edge):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))

# # 알고리즘
# def dijkstra(start, end):
#     initialization()
#     q = [] # priority q
#     heapq.heappush(q, (0, start)) # (거리, start)
#     distance[start] = 0
#     while q:
#         dist, current_node = heapq.heappop(q)
#         if distance[current_node] < dist:
#             continue
#         for i in graph[current_node]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost 
#                 heapq.heappush(q, (cost, i[0]))
#     result = distance[end]
#     return result

# X, K = map(int, input().split())

# result_1 = dijkstra(1, K)
# result_2 = dijkstra(K, X)
# total_distance = result_1 + result_2
# if total_distance >= INF:
#     print("INFINITY")
# else:
#     print(total_distance)

# ------플로이드 워셜 version-------
INF = int(1e9)

node, edge = map(int, input().split())
graph = [[INF] * (node + 1) for _ in range(node + 1)]

# 자기 자신은 0으로 초기화
for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

total_distance = graph[1][K] + graph[K][X]

if total_distance >= INF:
    print(-1)
else:
    print(total_distance)