import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (N - K + 1)
    dp[0] = sum(arr[:K])
    for i in range(1, N - K + 1):
        dp[i] = dp[i - 1] - arr[i - 1] + arr[i + K - 1]
    print(max(dp))


if __name__ == '__main__':
    main()
