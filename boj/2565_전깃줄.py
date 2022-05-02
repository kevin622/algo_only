import sys

input = sys.stdin.readline
N = int(input())
connections = [list(map(int, input().split())) for _ in range(N)]
connections.sort(key=lambda x: x[0])
right_dp = [0] * (max(connections, key=lambda x: x[1])[1] + 1)
for i in range(N):
    _, a = connections[i]
    right_dp[a] = max(right_dp[:a]) + 1
print(N - max(right_dp))
