import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N + 1)]
dp[1][0] = arr[0]
for i in range(2, N + 1):
    if i == 2:
        dp[i][0] = dp[i - 1][0] + arr[i - 1]
    else:
        dp[i][0] = dp[i - 1][1] + arr[i - 1]
    dp[i][1] = max(dp[i - 2]) + arr[i - 1]
print(max(dp[-1]))
