import sys

input = sys.stdin.readline


def print_(x):
    sys.stdout.write(f'{x} ')


N, M, K = map(int, input().split())
connections = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    n1, n2 = map(int, input().split())
    connections[n1].append(n2)
    connections[n2].append(n1)
for i in range(1, N + 1):
    connections[i].sort()
# DFS
visited = [0] * (N + 1)


def dfs(v: int):
    visited[v] = 1
    print_(v)
    for next_v in connections[v]:
        if not visited[next_v]:
            dfs(next_v)


dfs(K)
print()
# BFS
from collections import deque


def bfs(v: int):
    queue = deque([v])
    visited = [0] * (N + 1)
    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = 1
            print_(v)
            for next_v in connections[v]:
                if not visited[next_v]:
                    queue.append(next_v)


bfs(K)
print()
