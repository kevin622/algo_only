N, M = map(int, input().split())
sel = [0] * M


def sol(idx, num):
    if idx == M:
        print(*sel)
        return
    for i in range(num, N + 1):
        sel[idx] = i
        sol(idx + 1, i + 1)


sol(0, 1)
