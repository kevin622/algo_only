import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp_asc = [0] * (max(arr) + 1)
dp_desc = [0] * (max(arr) + 1)
arr_asc = [0] * N
arr_desc = [0] * N

for i in range(N):
    num = arr[i]
    dp_asc[num] = max(dp_asc[:num]) + 1
    arr_asc[i] = dp_asc[num]

    num = arr[N - i - 1]
    dp_desc[num] = max(dp_desc[:num]) + 1
    arr_desc[N - i - 1] = dp_desc[num]

answer = 0
for i in range(N):
    answer = max(arr_asc[i] + arr_desc[i], answer)

# print(f'arr: {arr}')
# print(f'arr_asc: {arr_asc}')
# print(f'arr_desc: {arr_desc}')
print(answer - 1)
