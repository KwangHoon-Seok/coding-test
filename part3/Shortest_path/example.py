# import heapq
# import sys

# # 빠른 입력 사용
# input = sys.stdin.readline
# INF = int(1e9)

# node, edge = map(int, input().split())
# start = int(input())

# # 그래프 정보 (a번 노드에서 b번 노드로 가는 가중치가 c)
# graph = [[] for _ in range(node + 1)]
# for _ in range(edge):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# # 최단 거리 테이블 (노드 번호 1~node까지 사용)
# distance = [INF] * (node + 1)

# def dijkstra(start):
#     q = []
#     # (최단 거리, 노드 번호) 순으로 힙에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         # 가장 최단 거리가 짧은 노드 정보 꺼내기
#         dist, now = heapq.heappop(q)

#         # 이미 처리된 적 있는 노드라면 무시 (방문 체크)
#         if distance[now] < dist:
#             continue

#         # 현재 노드와 연결된 다른 인접 노드 확인
#         for next_node in graph[now]:
#             target_node = next_node[0]
#             weight = next_node[1]
#             cost = dist + weight

#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
#             if cost < distance[target_node]:
#                 distance[target_node] = cost
#                 heapq.heappush(q, (cost, target_node))

# # 실행
# dijkstra(start)

# # 모든 노드로 가기 위한 최단 거리 출력
# for i in range(1, node + 1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# ------------ 플로이드 ------------# 
INF = 1e9
n = int(input())
m = int(input())

# 2차원 리스트 
graph = [[INF] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c # a -> b = c

# 대각 원소 0 
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] == 0

# 플로이드 
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

