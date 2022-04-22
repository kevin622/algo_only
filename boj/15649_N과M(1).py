N, M = map(int, input().split())
sel = [0] * M
selected = [0] * (N + 1)


def sol(idx):
    if idx == M:
        print(*sel)
        return
    for i in range(1, N + 1):
        if not selected[i]:
            sel[idx] = i
            selected[i] = 1
            sol(idx + 1)
            selected[i] = 0


sol(0)
