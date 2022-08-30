import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    sys.setrecursionlimit(N + 5)
    connections = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)

    dp = [[0, 1] for _ in range(N + 1)]

    def fill_dp(node: int = 1, parent: int = 0):
        for child in connections[node]:
            if child != parent:
                fill_dp(child, node)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child])

    fill_dp()
    print(min(dp[1]))


if __name__ == '__main__':
    main()
