import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N = int(input())
    roots = [0] * (N + 1)
    connections = {i: [] for i in range(1, N + 1)}
    for _ in range(N - 1):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)
    queue = deque([(1, 1)])
    while queue:
        root, v = queue.popleft()
        if roots[v] == 0:
            roots[v] = root
            for next_v in connections[v]:
                if roots[next_v] == 0:
                    queue.append((v, next_v))
    print('\n'.join(map(str, roots[2:])))


if __name__ == '__main__':
    main()
