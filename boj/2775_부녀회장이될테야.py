import sys


def main():
    input = sys.stdin.readline
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        n = int(input())
        dp = [list(range(n + 1))]
        dp.extend([[0] * (n + 1)] * k)
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[k][n])


if __name__ == "__main__":
    main()
