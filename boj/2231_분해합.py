N = int(input())


def get_decompose_sum(n: int) -> int:
    decomposed = map(lambda x: int(x), str(n))
    return n + sum(decomposed)


answer = 0
for i in range(1, N):
    if get_decompose_sum(i) == N:
        answer = i
        break
print(answer)
