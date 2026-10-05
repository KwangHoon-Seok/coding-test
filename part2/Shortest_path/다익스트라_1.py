import sys
input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
start = int(input())
# 2차원 테이블 생성 -> 노드끼리 어떤식으로 연결되어있는지 확인
graph = [[] for _ in range(node + 1)]
# visited 테이블 생성 -> 방문한 노드 체크 
visited = [False] * (node + 1)
# 최단거리 테이블 
distance = [INF] * (node + 1)

for _ in range(edge):
    # a에서 b로 가는 비용 c 
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 최단 거리 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1, node+1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대한 설정
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(node - 1):
        current_node = get_smallest_node()
        visited[current_node] = True
        for j in graph[current_node]:
            cost = distance[current_node] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])