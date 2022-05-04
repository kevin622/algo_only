import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[0])  # W, V
    arr = [[0, 0]] + arr
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        w, v = arr[i]
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j]
            if w <= j:
                dp[i][j] = max(v + dp[i - 1][j - w], dp[i][j])
    print(dp[N][K])


if __name__ == '__main__':
    main()
