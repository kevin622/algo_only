import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    rgbs = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    answer = INF
    for first_val in range(3):
        dp = [[0, 0, 0] for _ in range(N)]
        for i in range(3):
            if i == first_val:
                dp[0][i] = rgbs[0][i]
                continue
            dp[0][i] = INF
        for i in range(1, N):
            dp[i][0] = rgbs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = rgbs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = rgbs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        for i in range(3):
            if i == first_val:
                continue
            answer = min(answer, dp[N - 1][i])
    print(answer)


if __name__ == "__main__":
    main()