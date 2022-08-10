import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    # dp[i][j] : i번째까지의 아이템으로, 코스트가 j일 때 얻을 수 있는 최대 메모리
    dp = [[0] * (sum(costs) + 1) for _ in range(N)]

    # 첫 행 채우기
    for i in range(costs[0], len(dp[0])):
        dp[0][i] = memories[0]

    answer = len(dp[0]) - 1  # sum(costs)
    for i in range(1, N):
        memory = memories[i]
        cost = costs[i]
        for j in range(len(dp[0])):
            if j < cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cost] + memory, dp[i - 1][j])
            if dp[i][j] >= M:
                answer = min(answer, j)

    print(answer)


if __name__ == '__main__':
    main()
