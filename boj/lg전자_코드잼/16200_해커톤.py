import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = sorted(map(int, input().split()))
    cnt = 0
    idx = 0
    while idx < N:
        cnt += 1
        idx += arr[idx]
    print(cnt)


if __name__ == "__main__":
    main()
