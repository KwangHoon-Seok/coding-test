INF = int(1e9)

node = int(input())
edge = int(input())

graph = [[INF] * (node + 1) for _ in range(node + 1)]

# 자기 자신의 경로 자체는 0으로 바꿈
for a in range(1, node+1):
    for b in range(1, node + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력
for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 O(N^3)
for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if graph[a][b] == "INF":
            print("INFINITY")
        else:
            print(graph[a][b], end = " ")
    print()