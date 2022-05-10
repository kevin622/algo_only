import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    for i in range(N):
        answer += arr[i] * (N - i)
    sys.stdout.write(str(answer))


if __name__ == '__main__':
    main()
