N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
breakpoint()
sel = [0] * (N // 2)

answer = 1e10


def solve(idx, last_num):
    if idx == (N // 2):
        global answer
        team_1_sum = 0
        for i in range(len(sel) - 1):
            for j in range(i + 1, len(sel)):
                team_1_sum += matrix[sel[i]][sel[j]] + matrix[sel[j]][sel[i]]

        n_sel = []
        for i in range(N):
            if i not in sel:
                n_sel.append(i)
        team_2_sum = 0
        for i in range(len(n_sel) - 1):
            for j in range(i + 1, len(n_sel)):
                team_2_sum += matrix[n_sel[i]][n_sel[j]] + matrix[n_sel[j]][n_sel[i]]
        answer = min(answer, abs(team_1_sum - team_2_sum))
        return
    for i in range(last_num + 1, N):
        sel[idx] = i
        solve(idx + 1, i)


solve(0, -1)
print(answer)
