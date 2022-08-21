import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    INF = 100000
    # dp[i][j]: i에서 j로 가는 최소비용
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    # paths[(i, j)]: i에서 j로 갈 때 거쳐야 하는 지점들
    paths = {(i, j): [i, j] for i in range(1, n + 1) for j in range(1, n + 1)}
    for _ in range(m):
        a, b, c = map(int, input().split())
        dp[a][b] = min(dp[a][b], c)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dp[i][j] > (dp[i][k] + dp[k][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
                    paths[(i, j)] = paths[(i, k)] + paths[(k, j)][1:]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
                continue
            if dp[i][j] == INF:
                dp[i][j] = 0
    for i in range(1, n + 1):
        print(*dp[i][1:])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == 0:
                print(0)
                continue
            print(len(paths[(i, j)]), *paths[(i, j)])


if __name__ == '__main__':
    main()
