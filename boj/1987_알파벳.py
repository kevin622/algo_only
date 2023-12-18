import sys

max_cnt = -1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

input = sys.stdin.readline
R, C = map(int, input().split())
matrix = []
for _ in range(R):
    matrix.append(input().rstrip())

first_letter = matrix[0][0]
visited_coor = [[0] * C for _ in range(R)]
visited_coor[0][0] = 1 << (ord(first_letter) - ord('A'))

stack = [(0, 0, 1, 1 << (ord(first_letter) - ord('A')))]  # r, c, depth, path

while stack:
    r, c, depth, path = stack.pop()
    if depth > max_cnt:
        max_cnt = depth
        if depth == 26:
            break
    for i in range(4):
        next_r = r + dy[i]
        next_c = c + dx[i]
        if 0 <= next_r < R and 0 <= next_c < C:
            letter = matrix[next_r][next_c]
            idx = ord(letter) - ord('A')
            if visited_coor[next_r][next_c] != (path | (1 << idx)):
                if not path & (1 << idx):
                    visited_coor[next_r][next_c] = path | (1 << idx)
                    stack.append((next_r, next_c, depth + 1, path | (1 << idx)))

print(max_cnt)
