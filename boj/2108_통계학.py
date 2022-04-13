import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]


# counting sort를 dict를 사용해서 풀어보자
count = {i: 0 for i in range(-4000, 4001)}
for num in arr:
    count[num] += 1
idx = 0
arr = []
max_cnt_val = 0
max_vals = []
for num in range(-4000, 4001):
    if count[num]:
        arr.extend([num] * count[num])
        if count[num] > max_cnt_val:
            max_cnt_val = count[num]
            max_vals = [num]
        elif count[num] == max_cnt_val:
            max_vals.append(num)

# 산술평균
mean = round(sum(arr) / N)
# 중앙값(N은 홀수)
median = arr[N // 2]
# 최빈값
mode = max_vals[0] if len(max_vals) == 1 else max_vals[1]
# 범위
range_ = arr[N - 1] - arr[0]

print(mean)
print(median)
print(mode)
print(range_)
