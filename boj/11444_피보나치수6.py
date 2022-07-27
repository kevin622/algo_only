import sys


def mat_multiply(mat1: list, mat2: list) -> list:
    new_mat = []
    for row in mat1:
        new_row = []
        for col in zip(*mat2):
            val = 0
            for i in range(len(row)):
                val += row[i] * col[i]
            new_row.append(val % 1000000007)
        new_mat.append(new_row)
    return new_mat


def mat_power(mat: list, power: int):
    if power == 1:
        return mat
    else:
        divided_mat = mat_power(mat, power // 2)
        multiplied_mat = mat_multiply(divided_mat, divided_mat)
        if power % 2 == 0:
            return multiplied_mat
        else:
            return mat_multiply(multiplied_mat, mat)


def main():
    n = int(sys.stdin.readline().rstrip())
    if n == 1:
        print(1)
        return
    mat = [
        [0, 1],
        [1, 1]
    ]
    new_mat = mat_power(mat, n - 1)
    sys.stdout.write(str(new_mat[1][1]))


if __name__ == '__main__':
    main()
