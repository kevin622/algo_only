import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        nums = [0] + list(map(int, sys.stdin.readline().split()))

        # 누적합
        for i in range(1, K + 1):
            nums[i] += nums[i - 1]

        # dp[n][m] = n부터 m까지 합치는 최소비용
        dp = [[0 for _ in range(K)] for _ in range(K)]
        for j in range(1, K):
            for i in range(K - j):
                dp[i][i + j] = min([dp[i][k] + dp[k + 1][i + j] for k in range(i, i + j)]) + \
                               nums[i + j + 1] - nums[i]
        print(dp[0][K - 1])


if __name__ == '__main__':
    main()
