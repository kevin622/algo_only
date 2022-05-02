import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (max(arr) + 1)

for num in arr:
    dp[num] = max(dp[:num]) + 1
print(max(dp))
