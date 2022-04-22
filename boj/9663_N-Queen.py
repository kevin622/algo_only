N = int(input())
used_cols = set()
used_r_diags = set()
used_l_diags = set()

answer = 0


def n_queen(r):
    if r == N:
        global answer
        answer += 1
        return
    for c in range(N):
        if c not in used_cols and (r - c) not in used_r_diags and (r + c) not in used_l_diags:
            used_cols.add(c)
            used_r_diags.add(r - c)
            used_l_diags.add(r + c)
            n_queen(r + 1)
            used_cols.remove(c)
            used_r_diags.remove(r - c)
            used_l_diags.remove(r + c)


n_queen(0)
print(answer)
