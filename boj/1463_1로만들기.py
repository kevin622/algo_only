import sys

input = sys.stdin.readline

N = int(input())
INF = int(1e6)
dp = [INF for _ in range(N + 1)]
arr = [N]
cnt = 0
while True:
    new_arr = []
    while arr:
        n = arr.pop()
        if cnt < dp[n]:
            dp[n] = cnt
            if n % 2 == 0:
                new_arr.append(n // 2)
            if n % 3 == 0:
                new_arr.append(n // 3)
            if n > 1:
                new_arr.append(n - 1)
    cnt += 1
    arr = new_arr
    if dp[1] != INF:
        break
print(dp[1])
