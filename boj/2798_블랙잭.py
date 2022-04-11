sel = [0, 0, 0]
indices = []

N, M = map(int, input().split())
answer = 0
nums = list(map(int, input().split()))


def comb(idx, start):
    if idx == 3:
        global answer
        if sum(sel) <= M and (M - sum(sel)) < (M - answer):
            answer = sum(sel)
    else:
        for i in range(start, len(nums), 1):
            sel[idx] = nums[i]
            comb(idx + 1, i + 1)


comb(0, 0)
print(answer)
