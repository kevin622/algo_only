N = int(input())
arr = ['666']


def distinct_num_cnt(arr: list) -> int:
    arr = list(set(map(int, arr)))
    return len(arr)


while True:
    new_arr = []
    for i in range(10):
        i = str(i)
        for num in arr:
            new_arr.append(num + i)
            new_arr.append(i + num)
    arr.extend(new_arr)
    arr = list(set(arr))
    if distinct_num_cnt(arr) >= N:
        break
arr = list(set(map(int, arr)))
arr.sort()
print(arr[N - 1])
