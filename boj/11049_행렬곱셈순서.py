import sys


def main():
    N = int(sys.stdin.readline())
    sizes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    for j in range(1, N):
        for i in range(N - j):
            dp[i][i + j] = min([dp[i][i + k] + dp[i + k + 1][i + j] +
                                sizes[i][0] * sizes[i + k][1] * sizes[i + j][1]
                                for k in range(j)])
    print(dp[0][N - 1])


if __name__ == '__main__':
    main()
