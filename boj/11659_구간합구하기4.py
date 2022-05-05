import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + arr[i - 1]
    for _ in range(M):
        i, j = map(int, input().split())
        print(dp[j] - dp[i - 1])


if __name__ == '__main__':
    main()
