import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    dp = [int(1e9)] * (1 << N)
    dp[0] = 0

    for i in range(1 << N):
        work_cnt = 0
        for j in range(N):
            if i & (1 << j):
                work_cnt += 1
        for j in range(N):
            if i & (1 << j) == 0:
                dp[i | (1 << j)] = min(dp[i | (1 << j)], dp[i] + costs[work_cnt][j])
    print(dp[-1])


if __name__ == "__main__":
    main()
