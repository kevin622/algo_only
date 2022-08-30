import sys


def fibonacci(n):
    cnt = 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1
    return dp[n], cnt


def main():
    N = int(sys.stdin.readline())
    print(*fibonacci(N))


if __name__ == '__main__':
    main()
