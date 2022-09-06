import sys


def get_char_idx(s: str):
    return ord(s) - ord('A')


message = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()

coors = dict()
mat = [[''] * 5 for _ in range(5)]
row_idx = 0
col_idx = 0
is_used = [0] * 26
for char in key:
    if not is_used[get_char_idx(char)]:
        coors[char] = (row_idx, col_idx)
        mat[row_idx][col_idx] = char
        col_idx += 1
        if col_idx == 5:
            row_idx += 1
            col_idx = 0
        is_used[get_char_idx(char)] = 1
for i in range(26):
    if not is_used[i]:
        char = chr(ord('A') + i)
        if char == 'J':
            continue
        coors[char] = (row_idx, col_idx)
        mat[row_idx][col_idx] = char
        col_idx += 1
        if col_idx == 5:
            row_idx += 1
            col_idx = 0
        is_used[get_char_idx(char)] = 1

# 글자 나누기
idx = 0
two_letters = []
while idx < len(message):
    letter1 = message[idx]
    letter2 = message[idx + 1] if idx + 1 < len(message) else 'X'
    if idx == len(message) - 1:
        two_letters.append(letter1 + letter2)
        break
    if letter1 == letter2:
        idx += 1
        if letter1 != 'X':
            letter2 = 'X'
        else:
            letter2 = 'Q'
    else:
        idx += 2
    two_letters.append(letter1 + letter2)

answer = []
for letter1, letter2 in two_letters:
    row1, col1 = coors[letter1]
    row2, col2 = coors[letter2]
    if row1 == row2:
        new_letter1 = mat[row1][(col1 + 1) % 5]
        new_letter2 = mat[row2][(col2 + 1) % 5]
    elif col1 == col2:
        new_letter1 = mat[(row1 + 1) % 5][col1]
        new_letter2 = mat[(row2 + 1) % 5][col2]
    else:
        new_letter1 = mat[row1][col2]
        new_letter2 = mat[row2][col1]
    answer.append(new_letter1 + new_letter2)
print(''.join(answer))
