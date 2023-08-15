# 아직 못 풂!!!
import sys

MAX_VAL = 1000000 * 16
input = sys.stdin.readline
N = int(input())
distances = [list(map(int, input().split())) for _ in range(N)]
dp = [[None] * (1 << N) for _ in range(N)]


def dfs(curr_node: int, visited: int):
    if visited == ((1 << N) - 1):
        if distances[curr_node][0] != 0:
            return distances[curr_node][0]
        return MAX_VAL

    if dp[curr_node][visited]:
        return dp[curr_node][visited]

    tmp = MAX_VAL
    for next_node in range(N):
        if not distances[curr_node][next_node]:
            continue
        if visited & (1 << next_node):
            continue
        tmp = min(
            tmp,
            dfs(next_node, visited | (1 << next_node)) + distances[curr_node][next_node]
        )
    dp[curr_node][visited] = tmp
    return tmp


print(dfs(curr_node=0, visited=1))
