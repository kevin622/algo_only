import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, N + 1):
        graph[i].sort()

    # bfs
    visited = [0] * (N + 1)
    queue = deque([R])
    cnt = 1
    while queue:
        r = queue.popleft()
        if not visited[r]:
            visited[r] = cnt
            cnt += 1
            for n_r in graph[r]:
                if not visited[n_r]:
                    queue.append(n_r)
    for i in range(1, N + 1):
        print(visited[i])


if __name__ == "__main__":
    main()
