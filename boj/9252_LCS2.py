import sys


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    N, M = map(len, (s1, s2))
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp_str = [[''] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                dp_str[i][j] = dp_str[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                dp_str[i][j] = max(dp_str[i - 1][j], dp_str[i][j - 1], key=len)
    print(dp[N][M])
    print(dp_str[N][M])


if __name__ == '__main__':
    main()
