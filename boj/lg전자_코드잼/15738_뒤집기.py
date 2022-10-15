import sys


def main():
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    input()
    curr_idx = K
    for _ in range(M):
        i = int(input())
        if i > 1:
            if curr_idx <= i:
                curr_idx = i - curr_idx + 1
        elif i < 0:
            if (curr_idx - N - 1) >= i:
                curr_idx = i - curr_idx + 2 * N + 1
    print(curr_idx)


if __name__ == '__main__':
    main()
