import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    sys.setrecursionlimit(N + 5)
    arr = [0] + list(map(int, input().split()))
    connections = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)

    dp = [[0, arr[i]] for i in range(N + 1)]

    def fill_dp(node: int = 1, parent: int = 0):
        for child in connections[node]:
            if child != parent:
                fill_dp(child, node)
                dp[node][0] += max(dp[child])
                dp[node][1] += dp[child][0]

    fill_dp()
    print(max(dp[1]))


if __name__ == '__main__':
    main()
