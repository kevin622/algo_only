import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    grades = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        if not dp[a - 1]:
            dp[a - 1] = sum(grades[:(a - 1)])
        if not dp[b]:
            dp[b] = sum(grades[:b])
        summed = dp[b] - dp[a - 1]
        answer = round(summed / (b - a + 1), 2)
        sys.stdout.write(f'{answer:.2f}\n')
    return 0


if __name__ == '__main__':
    main()
