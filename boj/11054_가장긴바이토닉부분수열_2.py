import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    dp_forward = [0] * 1001
    dp_backward = [0] * 1001
    dp_answer = [0] * N
    for i in range(N):
        elem = A[i]
        dp_forward[elem] = max(dp_forward[:elem]) + 1
        dp_answer[i] = dp_forward[elem]
    for i in range(N - 1, -1, -1):
        elem = A[i]
        dp_backward[elem] = max(dp_backward[:elem]) + 1
        dp_answer[i] += dp_backward[elem]
    print(max(dp_answer) - 1)


if __name__ == "__main__":
    main()
