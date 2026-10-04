N, M = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

d = [10001] * (M + 1)

d[0] = 0

for coin in coins:
    for k in range(coin, M + 1):
        if d[k - coin] != 10001:
            d[k] = min(d[k], d[k - coin] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])