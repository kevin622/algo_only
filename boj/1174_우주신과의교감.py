import sys
from heapq import heappop, heappush


def get_head(x: int, heads: list[int]):
    if heads[x] != x:
        heads[x] = get_head(heads[x], heads)
    return heads[x]


def is_same_head(x: int, y: int, heads: list[int]):
    x_head = get_head(x, heads)
    y_head = get_head(y, heads)
    return x_head == y_head


def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    coors = [(0, 0)]
    for _ in range(N):
        X, Y = map(int, input().split())
        coors.append((X, Y))
    heads = list(range(N + 1))

    for _ in range(M):
        X, Y = map(int, input().split())
        X, Y = min(X, Y), max(X, Y)
        heads[get_head(Y, heads)] = get_head(X, heads)

    distances = []
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            x1, y1 = coors[i]
            x2, y2 = coors[j]
            distance = get_distance(x1, y1, x2, y2)
            distances.append((distance, i, j))
    distances.sort()

    answer = 0
    for dis, node1, node2 in distances:
        if is_same_head(node1, node2, heads):
            continue
        node1, node2 = min(node1, node2), max(node1, node2)
        heads[get_head(node2, heads)] = get_head(node1, heads)
        answer += dis

    print(f"{answer:.2f}")


if __name__ == "__main__":
    main()
