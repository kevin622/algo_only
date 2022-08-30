import sys


def main():
    input = sys.stdin.readline

    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        for _ in range(M):
            input()
        print(N - 1)


if __name__ == '__main__':
    main()
