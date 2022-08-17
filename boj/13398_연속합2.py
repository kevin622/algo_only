import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    dp_0 = [0] * N
    dp_1 = [0] * N
    answer = dp_0[0] = dp_1[0] = arr[0]
    for i in range(1, N):
        dp_0[i] = max(dp_0[i - 1] + arr[i], arr[i])
        dp_1[i] = max(dp_1[i - 1] + arr[i], dp_0[i - 1])
        answer = max(answer, dp_0[i], dp_1[i])
    print(answer)


if __name__ == '__main__':
    main()
