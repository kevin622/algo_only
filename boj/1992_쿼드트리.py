import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
answer = ''


def solve(r, c, n):
    global answer
    cnt = {'0': 0, '1': 0}
    for i in range(n):
        for j in range(n):
            cnt[matrix[r + i][c + j]] += 1
    if cnt['0'] == 0:
        answer += '1'
    elif cnt['1'] == 0:
        answer += '0'
    else:
        answer += '('
        half_n = n // 2
        solve(r, c, half_n)
        solve(r, c + half_n, half_n)
        solve(r + half_n, c, half_n)
        solve(r + half_n, c + half_n, half_n)
        answer += ')'


solve(0, 0, N)
sys.stdout.write(answer)
