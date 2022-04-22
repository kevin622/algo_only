N, M = map(int, input().split())
sel = [0] * M


def comb(idx, num):
    if idx == M:
        print(*sel)
        return
    for i in range(num, N + 1):
        sel[idx] = i
        comb(idx + 1, i)


comb(0, 1)
