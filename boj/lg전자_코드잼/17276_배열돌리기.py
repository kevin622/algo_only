import sys


def print_arr(arr: list[list]):
    for row in arr:
        print(*row)


def rotate_positive_arr(arr: list, n: int, d: int):
    mat = [row[:] for row in arr]
    while d > 0:
        for i in range(n):
            mat[i][i] = arr[n // 2][i]
            mat[i][n // 2] = arr[i][i]
            mat[i][n - i - 1] = arr[i][n // 2]
            mat[n // 2][i] = arr[n - i - 1][i]
        d -= 45
        arr = [row[:] for row in mat]
    return mat


def rotate_negative_arr(arr: list, n: int, d: int):
    mat = [row[:] for row in arr]
    while d < 0:
        for i in range(n):
            mat[i][i] = arr[i][n // 2]
            mat[i][n // 2] = arr[i][n - i - 1]
            mat[i][n - i - 1] = arr[n // 2][n - i - 1]
            mat[n // 2][i] = arr[i][i]
        d += 45
        arr = [row[:] for row in mat]
    return mat


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, d = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        if abs(d) == 360 or d == 0:
            print_arr(arr)
            continue
        mat = rotate_positive_arr(arr, n, d) if d > 0 else rotate_negative_arr(arr, n, d)
        print_arr(mat)


if __name__ == "__main__":
    main()
