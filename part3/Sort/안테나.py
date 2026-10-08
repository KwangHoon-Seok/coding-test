import sys

# 빠른 입력 사용
n = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))

# 1. 집의 위치를 오름차순으로 정렬
houses.sort()

# 2. 중앙값(Median) 위치의 집 출력
# N이 짝수일 때 동일한 최소 거리 중 더 작은 값을 요구하므로 (N - 1) // 2 인덱스를 선택
print(houses[(n - 1) // 2])