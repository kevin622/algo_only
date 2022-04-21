N = int(input())
answer = 0
i = 1
while N > (5 ** i):
    answer += N // (5 ** i)
    i += 1
print(answer)