import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]


def solve(r: int, c: int, n: int):
    cnt = [0, 0]
    for i in range(n):
        for j in range(n):
            cnt[matrix[r + i][c + j]] += 1
    if cnt[0] == 0:
        answer[1] += 1
        return
    elif cnt[1] == 0:
        answer[0] += 1
        return
    half_n = n // 2
    solve(r, c, half_n)
    solve(r + half_n, c, half_n)
    solve(r, c + half_n, half_n)
    solve(r + half_n, c + half_n, half_n)


solve(0, 0, N)
print(answer[0])
print(answer[1])
