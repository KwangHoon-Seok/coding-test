# from collections import deque

# # 입력 조건들
# N, M, K, X = map(int, input().split())
# graph = [[] for _ in range(N + 1)] # node 만큼의 graph 수
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# # 거리 초기화
# distance = [-1] * (N + 1)
# distance[X] = 0

# # bfs 구현
# q = deque([X])
# while q:
#     now = q.popleft()
#     for next_node in graph[now]:
#         if distance[next_node] == -1:
#             distance[next_node] = distance[now] + 1 # 가중치 1이기 때문에
#             q.append(next_node)

# # 출력
# check = False
# for i in range(1, N+1):
#     if distance[i] == K:
#         print(i)
#         check = True
# if check == False:
#     print(-1)


from collections import deque
node, edge, k, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for _ in range(node+1):
    a, b = map(int, input().split())
    graph[a].append(b) # a node에 연결된 노드들 다 넣기

distance = [-1] * (node + 1)
distance[start] = 0

q = deque[start]
while q:
    now = q.popleft() # 현재 노드 살핌
    for next_node in now:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)


# 출력
check = False
for i in range(1, node+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)