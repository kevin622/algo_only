T = int(input())
arr = [int(input()) for _ in range(T)]
N = max(arr)
dp_0 = [0] * (N + 1)
dp_0[0] = 1
dp_1 = [0] * (N + 1)
dp_1[1] = 1
for i in range(2, N + 1):
    dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
    dp_1[i] = dp_1[i - 1] + dp_1[i - 2]
for num in arr:
    print(dp_0[num], dp_1[num])
