import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * N
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    idx = max(dp)
    answer = []
    for i in range(N - 1, -1, -1):
        if dp[i] == idx:
            answer.append(arr[i])
            idx -= 1
    print(max(dp) + 1)
    print(*answer[::-1])


if __name__ == '__main__':
    main()
