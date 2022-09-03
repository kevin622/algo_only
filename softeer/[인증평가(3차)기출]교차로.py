import sys
from collections import deque


def get_car_idx(s: str):
    return ord(s) - ord('A')


def main():
    input = sys.stdin.readline
    N = int(input())
    queues = [deque([]), deque([]), deque([]), deque([])]
    for i in range(N):
        t, w = input().split()
        t = int(t)
        queues[get_car_idx(w)].append((i, t))

    answer = [-1] * N
    curr_time = -1
    is_waiting = [0, 0, 0, 0]
    while queues[0] or queues[1] or queues[2] or queues[3]:
        min_time = 1000000000
        for i in range(4):
            if queues[i]:
                time = queues[i][0][1]
                min_time = min(min_time, time)
                if time <= curr_time:
                    is_waiting[i] = 1
        num_waiting_cars = sum(is_waiting)
        # 교착 상태
        if num_waiting_cars == 4:
            break
        # 새 차가 하나도 없는 상태
        if num_waiting_cars == 0:
            curr_time = min_time
            continue
        for i in range(4):
            if is_waiting[i] and not is_waiting[(i - 1) % 4]:
                idx, _ = queues[i].popleft()
                answer[idx] = curr_time
        for i in range(4):
            is_waiting[i] = 0
        curr_time += 1
    print(*answer, sep='\n')


if __name__ == '__main__':
    main()
