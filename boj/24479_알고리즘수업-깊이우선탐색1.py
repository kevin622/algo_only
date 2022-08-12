import sys

input = sys.stdin.readline
sys.setrecursionlimit(200020)

N, M, R = map(int, input().split())
connection = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

for i in range(1, N + 1):
    connection[i].sort()

visited = [0] * (N + 1)
answer = [0] * (N + 1)
order = 1


def dfs(r: int):
    global order
    visited[r] = 1
    answer[r] = order
    order += 1
    for next_r in connection[r]:
        if not visited[next_r]:
            dfs(next_r)


dfs(R)
for i in range(1, N + 1):
    print(answer[i])
