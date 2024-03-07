import sys


def main():
    input = sys.stdin.readline
    N = int(input().strip())
    A = list(map(int, input().split()))
    dp = [0] * 1001
    for a in A:
        dp[a] = max(dp[:a]) + 1
    print(max(dp))


if __name__ == "__main__":
    main()
