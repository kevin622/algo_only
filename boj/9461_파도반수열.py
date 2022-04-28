T = int(input())
nums = [int(input()) for _ in range(T)]
N = max(nums)
dp = [0] * (N + 1)
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, N + 1):
    dp[i] = dp[i-2] + dp[i-3]

for num in nums:
    print(dp[num])


