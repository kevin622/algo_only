import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

    # bfs
    queue = deque([(0, 0, 0, 1)])
    while queue:
        r, c, did_break, cnt = queue.popleft()
        if not visited[r][c][did_break]:
            visited[r][c][did_break] = cnt
            for i in range(4):
                n_r = r + dy[i]
                n_c = c + dx[i]
                if 0 <= n_r < N and 0 <= n_c < M:
                    if not visited[n_r][n_c][did_break]:
                        if matrix[n_r][n_c] == 0:
                            queue.append((n_r, n_c, did_break, cnt + 1))
                    if not did_break and matrix[n_r][n_c] == 1:
                        queue.append((n_r, n_c, 1, cnt + 1))
    no_break_val, did_break_val = visited[N - 1][M - 1]
    if no_break_val > 0 and did_break_val > 0:
        print(min(no_break_val, did_break_val))
    elif no_break_val > 0 or did_break_val > 0:
        print(no_break_val or did_break_val)
    else:
        print(-1)


if __name__ == "__main__":
    main()
