import sys


def main():
    N = int(sys.stdin.readline())
    INF = int(1e9)
    dp1 = [INF] * (N + 1)
    dp1[1] = 0
    dp2 = [0] * (N + 1)
    for i in range(1, N):
        if dp1[i + 1] > (dp1[i] + 1):
            dp1[i + 1] = dp1[i] + 1
            dp2[i + 1] = i
        if (2 * i) <= N and dp1[2 * i] > (dp1[i] + 1):
            dp1[2 * i] = dp1[i] + 1
            dp2[2 * i] = i
        if (3 * i) <= N and dp1[3 * i] > (dp1[i] + 1):
            dp1[3 * i] = dp1[i] + 1
            dp2[3 * i] = i
    print(dp1[N])
    answer = [N]
    while N > 1:
        answer.append(dp2[N])
        N = dp2[N]
    print(*answer)


if __name__ == '__main__':
    main()
