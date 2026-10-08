def dfs(numbers, target, idx, total):
    if idx == len(numbers):
        if total == target:
            return 1
        else:
            return 0
    plus = dfs(numbers, target, idx + 1, total + numbers[idx])
    minus = dfs(numbers, target, idx + 1, total - numbers[idx])
    return plus + minus

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)


numbers = list(map(int, input().split()))
target = int(input())