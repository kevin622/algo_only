import sys

input = sys.stdin.readline


def mat_mul(mat1: list, mat2: list) -> list:
    new_mat = []
    for row in mat1:
        new_row = []
        for col in zip(*mat2):
            val = 0
            for i in range(len(mat1)):
                val += row[i] * col[i]
            val %= 1000
            new_row.append(val)
        new_mat.append(new_row)
    return new_mat


def mat_power(mat: list, power: int):
    if power == 1:
        new_mat = [[0] * len(mat) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat)):
                new_mat[i][j] = mat[i][j] % 1000
        return new_mat
    else:
        divided_mat = mat_power(mat, power // 2)
        if power % 2 == 0:
            return mat_mul(divided_mat, divided_mat)
        else:
            return mat_mul(mat_mul(divided_mat, divided_mat), mat)


def main():
    N, B = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    answer = mat_power(mat, B)
    for row in answer:
        print(*row)


if __name__ == '__main__':
    main()
