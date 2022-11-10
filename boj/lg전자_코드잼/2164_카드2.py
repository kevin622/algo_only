import sys


def main():
    N = int(sys.stdin.readline())
    if N <= 4:
        print(N)
        return
    num = 8
    while num < N:
        num *= 2
    print(2 * N - num)


if __name__ == '__main__':
    main()
