import sys


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    answer = 0
    for i in range(N - 1, -1, -1):
        if arr[i] <= K:
            answer += K // arr[i]
            K %= arr[i]
            if K == 0:
                break
    sys.stdout.write(f'{answer}')
    return 0


if __name__ == '__main__':
    main()
