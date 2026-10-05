# 최단 경로 알고리즘

가장 짧은 경로를 찾는 알고리즘. 상황에 따라 적합한 알고리즘이 다르다.


| 상황                              | 알고리즘      | 시간복잡도 |
| --------------------------------- | ------------- | ---------- |
| 한 지점 → 다른 모든 지점         | 다익스트라    | O(E log V) |
| 모든 지점 → 모든 지점            | 플로이드 워셜 | O(V³)     |
| 음수 간선이 있을 때 (단일 시작점) | 벨만-포드     | O(VE)      |

---

## 다익스트라 최단 경로 (그리디 알고리즘의 한 종류)

1. 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
2. **"음의 간선"이 없을 경우** 동작
   * 음수 간선이 있으면 "이미 확정한 최단거리가 나중에 더 줄어들 수 있다"는 모순이 생겨 그리디 선택이 깨진다
3. 매 상황에서 가장 비용이 적은 노드를 선택하므로 그리디 알고리즘으로 분류된다

### 알고리즘

1. 출발 노드 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3과 4번 반복

### 핵심 아이디어

* 한 번 선택되어 처리된 노드의 최단 거리는 **그 시점에 확정**된다
* 따라서 각 노드는 단 한 번만 처리하면 된다
* 테이블에는 "현재까지 알아낸 가장 짧은 거리"가 계속 갱신되며 쌓인다

### 자료구조: 인접 리스트

```python
graph = [[] for _ in range(n + 1)]
graph[a].append((b, c))   # a에서 b로 가는 비용 c
```

"현재 노드의 이웃을 순회"하는 것이 주 연산이라 인접 리스트가 유리하다.

### 구현 1. 간단한 구현 — O(V²)

매 단계마다 전체 노드를 선형 탐색해서 최단 거리 노드를 찾는 방식.

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for b, c in graph[start]:
        distance[b] = min(distance[b], c)

    # 시작 노드를 제외한 n-1개의 노드에 대해 반복
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost

dijkstra(start)

for i in range(1, n + 1):
    print("INFINITY" if distance[i] == INF else distance[i])
```

노드 개수가 5,000 이하일 때 사용 가능. 그 이상이면 시간 초과.

### 구현 2. 우선순위 큐 — O(E log V)

최단 거리가 가장 짧은 노드를 **힙(heap)** 에서 O(log V)에 꺼내는 방식. 실전에서는 이쪽을 쓴다.

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # (거리, 노드) 순서 — 거리 기준 정렬
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 더 짧은 경로로 처리된 노드라면 무시 (방문 처리 대체)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

dijkstra(start)

for i in range(1, n + 1):
    print("INFINITY" if distance[i] == INF else distance[i])
```

**포인트**

* 튜플을 `(거리, 노드)` 순서로 넣어야 거리 기준으로 정렬된다
* 파이썬 `heapq`는 최소 힙이므로 그대로 쓰면 된다
* `visited` 배열 대신 `if distance[now] < dist: continue` 로 처리한다
* 같은 노드가 큐에 여러 번 들어갈 수 있지만, 위 조건으로 걸러지므로 문제없다

---

## 플로이드 워셜 알고리즘 (다이나믹 프로그래밍)

1. **모든 노드에서 다른 모든 노드까지의** 최단 경로를 모두 계산
2. 2차원 테이블에 최단 거리 정보를 저장
3. 음수 간선이 있어도 동작한다 (단, 음수 사이클은 불가)

### 핵심 아이디어

> i에서 j로 갈 때, **k를 거쳐 가는 것이 더 싼가?**

```
D[i][j] = min(D[i][j], D[i][k] + D[k][j])
```

k 루프를 **가장 바깥**에 두는 것이 핵심이다. k는 단순한 반복 변수가 아니라 **"경유지로 사용을 허가한 노드 집합"** 이라는 DP의 단계를 의미한다.

* k=1 단계 종료 시: 1번만 경유지로 써도 되는 최단거리
* k=2 단계 종료 시: 1, 2번만 경유지로 써도 되는 최단거리
* k=n 단계 종료 시: 모든 노드를 경유지로 쓸 수 있는 진짜 최단거리

1\~k는 "거쳐야 하는 노드"가 아니라 **"거쳐도 되는 후보"** 다. 직행이 가장 싸면 그게 답이다.

### 알고리즘

1. 2차원 테이블을 INF로 초기화
2. 자기 자신으로 가는 비용은 0으로 설정
3. 주어진 간선 정보를 테이블에 입력
4. 경유지 k를 1부터 n까지 늘려가며 모든 (a, b) 쌍을 갱신

### 자료구조: 인접 행렬

```python
graph = [[INF] * (n + 1) for _ in range(n + 1)]
graph[a][b] = c
```

"임의의 두 점 사이 값을 O(1)에 조회/수정"하는 것이 주 연산이라 인접 행렬이 필요하다.

> ⚠️ `[[INF] * (n+1)] * (n+1)` 로 쓰면 안 된다. 같은 리스트 객체가 참조되어 한 칸만 바꿔도 모든 행이 함께 바뀐다. 반드시 리스트 컴프리헨션을 쓸 것.

### 구현

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력 (중복 간선 대비해 min 처리)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 수행
for k in range(1, n + 1):          # 경유지
    for a in range(1, n + 1):      # 출발
        for b in range(1, n + 1):  # 도착
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print("INFINITY" if graph[a][b] == INF else graph[a][b], end=" ")
    print()
```

### 음수 사이클 탐지

알고리즘 수행 후 `graph[i][i] < 0` 인 i가 존재하면 음수 사이클이 있다는 뜻이다. 자기 자신으로 돌아왔는데 비용이 줄었다는 것은 돌수록 싸진다는 의미이기 때문이다.

---

## 공통 주의사항

### 1. 배열 크기는 `n + 1`

노드 번호가 1부터 시작하므로 인덱스를 맞추기 위해 한 칸 더 잡는다. 0번 자리는 쓰지 않고 버린다. 메모리를 조금 낭비하는 대신 `-1` 변환 실수를 원천 차단할 수 있다.

```python
distance = [INF] * (n + 1)
for i in range(1, n + 1):   # 1 ~ n 이 그대로 유효한 인덱스
```

### 2. INF 값 설정

`int(1e9)` 정도가 무난하다. 너무 크게 잡으면 `INF + INF` 연산 시 오버플로우 위험이 있다 (파이썬은 안전하지만 C++/Java에서는 주의).

### 3. 입력이 많을 때

```python
import sys
input = sys.stdin.readline
```

간선 개수가 수만 개 이상이면 기본 `input()` 은 느려서 시간 초과가 날 수 있다.

### 4. 단방향 / 양방향 구분

문제에서 양방향 간선이라고 하면 반대 방향도 넣어야 한다.

```python
graph[a].append((b, c))
graph[b].append((a, c))   # 양방향일 때만
```

---

## 어떤 것을 선택할까

```
시작점이 하나인가?
├─ 예 → 음수 간선이 있는가?
│        ├─ 아니오 → 다익스트라 (우선순위 큐)
│        └─ 예     → 벨만-포드
└─ 아니오 (모든 쌍 필요) → 노드 수가 500 이하인가?
                           ├─ 예     → 플로이드 워셜
                           └─ 아니오 → 다익스트라를 V번 반복
```
