import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    N, M = map(int, input().split())
    matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
    matrix = [[0] * (N + 1)] + matrix
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1])


if __name__ == '__main__':
    main()
