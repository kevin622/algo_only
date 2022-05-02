import sys


def main():
    first_str = sys.stdin.readline().rstrip()
    second_str = sys.stdin.readline().rstrip()
    dp = [[0] * (len(second_str) + 1) for _ in range(len(first_str) + 1)]
    for i in range(len(first_str)):
        a = first_str[i]
        for j in range(len(second_str)):
            b = second_str[j]
            if a == b:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    print(dp[len(first_str)][len(second_str)])


if __name__ == '__main__':
    main()
