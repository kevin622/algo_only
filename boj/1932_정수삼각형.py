import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
for _ in range(N - 1):
    new_arr = list(map(int, input().split()))
    new_arr[0] += arr[0]
    new_arr[-1] += arr[-1]
    for i in range(1, len(new_arr) - 1):
        new_arr[i] += max(arr[i - 1], arr[i])
    arr = new_arr
print(max(arr))
