import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
count_dict = dict()
count_dict[sorted_arr[0]] = 0
last_cnt = 0
for i in range(1, len(sorted_arr)):
    if sorted_arr[i] == sorted_arr[i - 1]:
        continue
    last_cnt += 1
    count_dict[sorted_arr[i]] = last_cnt
print(' '.join(map(lambda x: str(count_dict[x]), arr)))
