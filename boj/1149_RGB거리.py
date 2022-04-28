N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    a, b, c = map(int, input().split())
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + b
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + c
print(min(dp[N]))
