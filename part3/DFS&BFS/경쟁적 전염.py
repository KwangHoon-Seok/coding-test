from collections import deque
N, K = map(int, input().split())
labs = []
virus_data = []
for i in range(N):
    labs.append(list(map(int, input().split())))
    for j in range(N):
        if labs[i][j] != 0:
            virus_data.append((labs[i][j], 0, i, j))
# 상하좌우
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

target_s, x, y = map(int, input().split())
target_x = x - 1
target_y = y - 1

result = 0

virus_data.sort()
virus_data_queue = deque(virus_data)
while virus_data_queue:
    virus, second, x, y = virus_data_queue.popleft()
    if second == target_s:
        result = labs[target_x][target_y]
        print(labs)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if labs[nx][ny] == 0:
                labs[nx][ny] = virus
                virus_data_queue.append((virus, second + 1, nx, ny))


print(result)