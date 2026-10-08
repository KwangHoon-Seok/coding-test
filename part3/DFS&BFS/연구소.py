# # bfs + dfs + 백트래킹

# import copy
# from collections import deque

# n, m = map(int, input().split())
# lab = []
# for _ in range(n):
#     lab.append(list(map(int, input().split())))

# # 방향 벡터 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# max_safe_area = 0

# # 바이러스 퍼뜨리기 (BFS)
# def virus_bfs():
#     global max_safe_area
#     # 벽이 세워진 연구소 지도 복사
#     temp_lab = copy.deepcopy(lab)
#     q = deque()

#     # 초기 바이러스 위치 큐에 삽입
#     for i in range(n):
#         for j in range(m):
#             if temp_lab[i][j] == 2:
#                 q.append((i, j))

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m:
#                 # 빈칸이면 바이러스 전파
#                 if temp_lab[nx][ny] == 0:
#                     temp_lab[nx][ny] = 2
#                     q.append((nx, ny))

#     # 안전 영역(0) 개수 세기
#     safe_area = 0
#     for i in range(n):
#         for j in range(m):
#             if temp_lab[i][j] == 0:
#                 safe_area += 1

#     max_safe_area = max(max_safe_area, safe_area)


# # 벽 3개를 세우는 재귀 함수 (DFS)
# def build_wall(count):
#     if count == 3:
#         virus_bfs()  # 벽 3개가 모두 세워지면 바이러스 시뮬레이션
#         return

#     for i in range(n):
#         for j in range(m):
#             if lab[i][j] == 0:
#                 lab[i][j] = 1  # 벽 세우기
#                 build_wall(count + 1)
#                 lab[i][j] = 0  # 원상 복구 (백트래킹)


# # 메인 실행
# build_wall(0)
# print(max_safe_area)

#--------------- 1 loop------------------#
from collections import deque
n, m = map(int, input().split())
# lab 지도 생성
lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

max_safty_area = 0
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
def virus():
    global max_safty_area
    virus_lab = lab
    q = deque()
    for i in range(n):
        for j in range(m):
            if virus_lab[i][j] == 2:
                q.append((i,j)) # 바이러스 위치 삽입
    # 바이러스 퍼뜨리기 bfs
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m:
                if virus_lab[nx][ny] == 0:
                    virus_lab[nx][ny] = 2
                    q.append((nx, ny))
    safety_area = 0
    for i in range(n):
        for j in range(m):
            if virus_lab[i][j] == 0:
                safety_area += 1
    max_safty_area = max(max_safty_area, safety_area)

def build_wall(count):
    if count == 3:
        virus()
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_wall(count + 1)
                lab[i][j]=0

build_wall(0)
print(max_safty_area)
                