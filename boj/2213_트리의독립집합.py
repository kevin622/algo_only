import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    sys.setrecursionlimit(n + 5)
    weights = {(i + 1): j for i, j in enumerate(map(int, input().split()))}
    connections = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)

    # make as tree using dfs
    tree = dict()

    def dfs(node: int):
        tree[node] = []
        for next_node in connections[node]:
            if next_node not in tree:
                tree[node].append(next_node)
                dfs(next_node)

    dfs(1)

    dp = [[0, 0] for _ in range(n + 1)]
    dp_path = [[[], []] for _ in range(n + 1)]

    def fill_dp(node: int):
        dp[node][1] = weights[node]
        dp_path[node][1].append(node)
        if not tree[node]:
            return
        for child_node in tree[node]:
            fill_dp(child_node)
            if dp[child_node][0] > dp[child_node][1]:
                dp[node][0] += dp[child_node][0]
                dp_path[node][0].extend(dp_path[child_node][0])
            else:
                dp[node][0] += dp[child_node][1]
                dp_path[node][0].extend(dp_path[child_node][1])
            dp[node][1] += dp[child_node][0]
            dp_path[node][1].extend(dp_path[child_node][0])

    fill_dp(1)
    if dp[1][0] > dp[1][1]:
        print(dp[1][0])
        print(*sorted(dp_path[1][0]))
    else:
        print(dp[1][1])
        print(*sorted(dp_path[1][1]))


if __name__ == '__main__':
    main()
