import sys


def main():
    input = sys.stdin.readline
    S = input().rstrip()
    N, M = map(int, input().split())
    mat = [input().rstrip() for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if M >= len(S) and (j + len(S)) <= M:
                # 왼쪽에서 오른쪽
                if mat[i][j:(j + len(S))] == S:
                    answer = 1
                    break
                # 오른쪽에서 왼쪽
                if mat[i][j:(j + len(S))][::-1] == S:
                    answer = 1
                    break
            if N >= len(S) and (i + len(S)) <= N:
                # 위에서 아래, 아래에서 위
                temp_s = ''
                for k in range(len(S)):
                    temp_s += mat[i + k][j]
                if temp_s == S or temp_s[::-1] == S:
                    answer = 1
            if M >= len(S) and N >= len(S) and (j + len(S)) <= M and (i + len(S)) <= N:
                temp_s = ''
                for k in range(len(S)):
                    # 왼쪽 위에서 오른쪽 아래, 오른쪽 아래에서 왼쪽 위
                    temp_s += mat[i + k][j + k]
                if temp_s == S or temp_s[::-1] == S:
                    answer = 1
                    break
                temp_s = ''
                for k in range(len(S)):
                    # 왼쪽 아래에서 오른쪽 위, 오른쪽 위에서 왼쪽 아래
                    temp_s += mat[i + len(S) - 1 - k][j + k]
                if temp_s == S or temp_s[::-1] == S:
                    answer = 1
                    break
            if answer:
                break
        if answer:
            break
    print(answer)


if __name__ == '__main__':
    main()
