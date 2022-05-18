A, B, C = map(int, input().split())


def solve(A, B, C):
    if B == 1:
        A %= C
        return A
    elif B == 0:
        return 1
    else:
        answer = (solve(A, B // 2, C) ** 2) * solve(A, B % 2, C)
        answer %= C
        return answer


print(solve(A, B, C))
