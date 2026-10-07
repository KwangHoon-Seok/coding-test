def solution(array):
    count = 0
    for c in array:
        if c == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return count == 0


arr = input()
print(solution(arr))
