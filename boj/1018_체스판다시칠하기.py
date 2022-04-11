arr1 = ['W', 'B'] * 4
arr2 = ['B', 'W'] * 4
good_mat1 = [arr1, arr2] * 4
good_mat2 = [arr2, arr1] * 4

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

answer = int(1e10)

for n in range(N - 7):
    for m in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if matrix[n + i][m + j] != good_mat1[i][j]:
                    cnt1 += 1
                if matrix[n + i][m + j] != good_mat2[i][j]:
                    cnt2 += 1
        answer = min(answer, cnt1, cnt2)
print(answer)
