import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    jumps = {}
    for _ in range(N + M):
        i, j = map(int, input().split())
        jumps[i] = j

    # bfs
    queue = deque([(1, 0)])
    visited = [0] * 101
    while queue:
        point, cost = queue.popleft()
        if not visited[point]:
            visited[point] = cost
            for i in range(1, 7):
                next_v = jumps[point + i] if (point + i) in jumps else point + i
                if next_v < 100 and not visited[next_v]:
                    queue.append((next_v, cost + 1))
                if next_v == 100:
                    print(cost + 1)
                    return


if __name__ == '__main__':
    main()
