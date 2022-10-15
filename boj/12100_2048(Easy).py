import sys
from copy import deepcopy

max_val = -1


def push_up(new_mat, N):
    for c in range(N):
        arr = []
        for r in range(N):
            if new_mat[r][c]:
                arr.append(new_mat[r][c])
                new_mat[r][c] = 0
        a_i = 0
        m_i = 0
        while a_i < len(arr):
            val = arr[a_i]
            if (a_i + 1) < len(arr) and arr[a_i + 1] == val:
                new_mat[m_i][c] = val * 2
                a_i += 2
            else:
                new_mat[m_i][c] = val
                a_i += 1
            m_i += 1
    return new_mat


def push_down(new_mat, N):
    for c in range(N):
        arr = []
        for r in range(N - 1, -1, -1):
            if new_mat[r][c]:
                arr.append(new_mat[r][c])
                new_mat[r][c] = 0
        a_i = 0
        m_i = N - 1
        while a_i < len(arr):
            val = arr[a_i]
            if (a_i + 1) < len(arr) and arr[a_i + 1] == val:
                new_mat[m_i][c] = val * 2
                a_i += 2
            else:
                new_mat[m_i][c] = val
                a_i += 1
            m_i -= 1
    return new_mat


def push_left(new_mat, N):
    for r in range(N):
        arr = []
        for c in range(N):
            if new_mat[r][c]:
                arr.append(new_mat[r][c])
                new_mat[r][c] = 0
        a_i = 0
        m_i = 0
        while a_i < len(arr):
            val = arr[a_i]
            if (a_i + 1) < len(arr) and arr[a_i + 1] == val:
                new_mat[r][m_i] = val * 2
                a_i += 2
            else:
                new_mat[r][m_i] = val
                a_i += 1
            m_i += 1
    return new_mat


def push_right(new_mat, N):
    for r in range(N):
        arr = []
        for c in range(N - 1, -1, -1):
            if new_mat[r][c]:
                arr.append(new_mat[r][c])
                new_mat[r][c] = 0
        a_i = 0
        m_i = N - 1
        while a_i < len(arr):
            val = arr[a_i]
            if (a_i + 1) < len(arr) and arr[a_i + 1] == val:
                new_mat[r][m_i] = val * 2
                a_i += 2
            else:
                new_mat[r][m_i] = val
                a_i += 1
            m_i -= 1
    return new_mat


def update_max_val(mat: list[list[int]], N: int, depth=0):
    global max_val
    if depth == 5:
        for arr in mat:
            max_val = max(max_val, max(arr))
        return
    new_mat = push_up(deepcopy(mat), N)
    update_max_val(new_mat, N, depth + 1)

    new_mat = push_left(deepcopy(mat), N)
    update_max_val(new_mat, N, depth + 1)

    new_mat = push_down(deepcopy(mat), N)
    update_max_val(new_mat, N, depth + 1)

    new_mat = push_right(deepcopy(mat), N)
    update_max_val(new_mat, N, depth + 1)


def main():
    input = sys.stdin.readline
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    update_max_val(mat, N)
    print(max_val)


if __name__ == '__main__':
    main()
