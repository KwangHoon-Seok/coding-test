import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
start = int(input())
graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    a,b,c = map(int, input().split()) # b, c = (연결 노드, 비용)
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) 
    distance[start] = 0
    while q:
        dist, current_node = heapq.heappop(q) # 현재 노드 정보 (거리, 노드)
        if distance[current_node] < dist:
            continue
        for i in graph[current_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]= cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])