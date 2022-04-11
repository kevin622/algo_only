N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
biggers = [1] * N
idx = 0
for x1, y1 in arr:
    cnt = 0
    for x2, y2 in arr:
        if x1 < x2 and y1 < y2:
            cnt += 1
    biggers[idx] += cnt
    idx += 1
print(*biggers)