import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))

    # dp[i][j] = i 부터 j까지 펠린드롬이면 1, 아니면 0
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1):
        if nums[i] == nums[i + 1]:
            dp[i][i + 1] = 1

    for i in range(2, N):
        for j in range(N - i):
            if dp[j + 1][j + i - 1] == 1 and nums[j] == nums[j + i]:
                dp[j][j + i] = 1

    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])


if __name__ == '__main__':
    main()
