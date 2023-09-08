import sys


def main():
    N = int(sys.stdin.readline())  # 4 ≤ N ≤ 1000
    K = int(sys.stdin.readline())  # 1 ≤ K ≤ N
    val = 1000000003
    if K == 1:
        print(N)
        return
    # f(n, k) = f(n-1, k) + f(n-2, k-1)
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        dp[n][1] = n
    for n in range(4, N + 1):
        for k in range(2, K + 1):
            if k > (n // 2):
                break
            dp[n][k] = (dp[n - 1][k] + dp[n - 2][k - 1]) % val
    print(dp[N][K])
    return


if __name__ == "__main__":
    main()
