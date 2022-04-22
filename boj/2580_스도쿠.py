import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
blanks = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            blanks.append([r, c])
num_of_blanks = len(blanks)


def solve_sudoku(idx):
    if idx == num_of_blanks:
        for row in board:
            print(' '.join(map(str, row)))
        exit(0)

    r, c = blanks[idx]
    candidates = get_candidates(r, c)
    for num in candidates:
        board[r][c] = num
        solve_sudoku(idx + 1)
        board[r][c] = 0


def get_candidates(r: int, c: int) -> list:
    candidates = list(range(1, 10))
    for i in range(9):
        # row
        if board[r][i] in candidates:
            candidates.remove(board[r][i])
        # column
        if board[i][c] in candidates:
            candidates.remove(board[i][c])
    # box
    first_r = (r // 3) * 3
    first_c = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            curr_num = board[first_r + i][first_c + j]
            if curr_num in candidates:
                candidates.remove(curr_num)
    return candidates


solve_sudoku(0)
