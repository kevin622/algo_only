import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    arr = [[i, (i - 2) % N, i % N] for i in range(1, N + 1)]
    answer = []
    cnt = 0
    idx = 0
    while cnt != N:
        for _ in range(K - 1):
            idx = arr[idx][2]
        answer.append(arr[idx][0])
        left = arr[idx][1]
        right = arr[idx][2]
        arr[left][2] = arr[idx][2]
        arr[right][1] = arr[idx][1]
        idx = right
        cnt += 1

    print('<', ', '.join(map(str, answer)), '>', sep='')


if __name__ == '__main__':
    main()
