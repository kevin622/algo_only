import sys

input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    INF = int(1e9)
    dis = [[INF] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        start, end, cost = map(int, input().split())
        dis[start][end] = cost

    # floyd-warshall
    for mid in range(1, V + 1):
        for start in range(1, V + 1):
            for end in range(1, V + 1):
                if dis[start][end] > (dis[start][mid] + dis[mid][end]):
                    dis[start][end] = dis[start][mid] + dis[mid][end]
    answer = INF
    for i in range(1, V + 1):
        answer = min(answer, dis[i][i])
    if answer == INF:
        print(-1)
    else:
        print(answer)


if __name__ == '__main__':
    main()
