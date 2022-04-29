import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n + 1)]  # [현재 잔 안 먹음, 앞 잔을 안 먹고 현재 잔 먹음, 앞 잔을 먹고 현재 잔 먹음]
dp[1] = [0, arr[0], arr[0]]
for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + arr[i - 1]
    dp[i][2] = dp[i - 1][1] + arr[i - 1]

print(max(dp[-1]))
