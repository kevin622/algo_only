import sys

input = sys.stdin.readline


def main():
    n = int(input())
    m = int(input())
    INF = int(1e9)
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0
    for _ in range(m):
        start, end, cost = map(int, input().split())
        distance[start][end] = min(distance[start][end], cost)

    # floyd-warshall
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if distance[start][end] > (distance[start][mid] + distance[mid][end]):
                    distance[start][end] = distance[start][mid] + distance[mid][end]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][j] == INF:
                distance[i][j] = 0
        print(*distance[i][1:])


if __name__ == '__main__':
    main()
