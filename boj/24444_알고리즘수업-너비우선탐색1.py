import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, M, R = map(int, input().split())
    connections = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        connections[u].append(v)
        connections[v].append(u)
    for i in range(1, N + 1):
        connections[i].sort()

    visited = [0] * (N + 1)
    queue = deque([R])
    order = 1
    while queue:
        r = queue.popleft()
        if not visited[r]:
            visited[r] = order
            order += 1
            for next_r in connections[r]:
                if not visited[next_r]:
                    queue.append(next_r)

    print('\n'.join(map(str, visited[1:])))


if __name__ == '__main__':
    main()
