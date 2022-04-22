N, M = map(int, input().split())
sel = [0] * M


def comb(idx):
    if idx == M:
        print(*sel)
        return
    for i in range(1, N + 1):
        sel[idx] = i
        comb(idx + 1)


comb(0)
