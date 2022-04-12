# O(n + k)
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'before: {arr}')


def counting_sort():
    max_val = max(arr)
    # counting 배열 만들기
    count_arr = [0] * (max_val + 1)
    for num in arr:
        count_arr[num] += 1
    # counting 배열 누적합으로 만들기
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    # 정렬된 배열이 될 temp
    temp = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        num = arr[j]
        count_arr[num] -= 1
        temp[count_arr[num]] = num
    return temp


arr = counting_sort()
print(f'after: {arr}')
