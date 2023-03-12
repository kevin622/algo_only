import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    in_degree = [0] * (N + 1)
    connections = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        connections[A].append(B)
        in_degree[B] += 1
    queue = deque([])
    answer = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        val = queue.popleft()
        answer.append(val)
        for next_val in connections[val]:
            in_degree[next_val] -= 1
            if in_degree[next_val] == 0:
                queue.append(next_val)
    print(*answer)


if __name__ == "__main__":
    main()
