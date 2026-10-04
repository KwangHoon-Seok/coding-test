N = int(input())
arr = list(map(int, input().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[N-1])

# 몇 번 터는 것에 대한 제약이 없다. 그러므로 제약식 성립