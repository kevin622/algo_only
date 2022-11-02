import sys


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    mat = [input().rstrip() for _ in range(N)]
    cnt = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (i + j) % 2 == 0:
                if mat[i - 1][j - 1] == 'B':
                    cnt[i][j] = cnt[i][j - 1] + 1
                else:
                    cnt[i][j] = cnt[i][j - 1]
            else:
                if mat[i - 1][j - 1] == 'B':
                    cnt[i][j] = cnt[i][j - 1]
                else:
                    cnt[i][j] = cnt[i][j - 1] + 1
        for j in range(1, M + 1):
            cnt[i][j] += cnt[i - 1][j]

    val = whole_cnt = K ** 2
    for i in range(K, N + 1):
        for j in range(K, M + 1):
            cnt1 = cnt[i][j] - cnt[i][j - K] - cnt[i - K][j] + cnt[i - K][j - K]
            cnt2 = whole_cnt - cnt1
            val = min(val, cnt1, cnt2)
    print(val)


if __name__ == '__main__':
    main()
