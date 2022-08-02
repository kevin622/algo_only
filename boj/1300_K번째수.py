import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    left = 1
    right = N * N
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(N, mid // i)
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    sys.stdout.write(str(left))


if __name__ == '__main__':
    main()
