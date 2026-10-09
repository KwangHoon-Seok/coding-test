n = int(input()) # 도시 (node)
m = int(input()) # 버스 (edge)
INF = 1e9 

# graph 초기 환경 세팅
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # a->b = c
    if c < graph[a][b]:
        graph[a][b] = c
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

