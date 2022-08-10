import sys

sys.setrecursionlimit(500 * 500)

M, N = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(r, c):
    if r == (M - 1) and c == (N - 1):
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for i in range(4):
        next_r = r + dy[i]
        next_c = c + dx[i]
        if 0 <= next_r < M and 0 <= next_c < N:
            if mat[next_r][next_c] < mat[r][c]:
                dp[r][c] += dfs(next_r, next_c)
    return dp[r][c]


def main():
    print(dfs(0, 0))


if __name__ == '__main__':
    main()
