N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_val = -int(1e10)
min_val = int(1e10)


def sign(n: int):
    if n == 0:
        return 1
    return n // abs(n)


def get_max(idx, num):
    if idx == N:
        global max_val, min_val
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    for i in range(4):
        if operators[i] > 0:
            if i == 0:
                next_num = num + arr[idx]
            elif i == 1:
                next_num = num - arr[idx]
            elif i == 2:
                next_num = num * arr[idx]
            elif i == 3:
                next_num = abs(num) // arr[idx] * sign(num)
            operators[i] -= 1
            get_max(idx + 1, next_num)
            operators[i] += 1


get_max(1, arr[0])
print(max_val)
print(min_val)
