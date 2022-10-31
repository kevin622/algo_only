import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def fill_mat(matrix, row, col, color, visited):
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        if not visited[row][col]:
            visited[row][col] = 1
            for i in range(4):
                n_row = row + dy[i]
                n_col = col + dx[i]
                if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]):
                    if matrix[n_row][n_col] == matrix[row][col] and not visited[n_row][n_col]:
                        queue.append((n_row, n_col))
            matrix[row][col] = color
    return

# def fill_mat(matrix, row, col, color, visited):
#     if not visited[row][col]:
#         visited[row][col] = 1
#         for i in range(4):
#             n_row = row + dy[i]
#             n_col = col + dx[i]
#             if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]):
#                 if matrix[n_row][n_col] == matrix[row][col] and not visited[n_row][n_col]:
#                     fill_mat(matrix, n_row, n_col, color, visited)
#         matrix[row][col] = color
#     return


def main():
    sys.setrecursionlimit(int(1e6))
    input = sys.stdin.readline
    H, W = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())
    for _ in range(Q):
        i, j, c = map(int, input().split())
        visited = [[0] * W for _ in range(H)]
        fill_mat(mat, i - 1, j - 1, c, visited)
    for row in mat:
        print(*row)


if __name__ == '__main__':
    main()
