import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
answer = 0
cnt = N
pos = 0
curr_val = nums[pos]
next_val = min(nums)
while cnt:
    # move right
    right_moving_pos = pos
    while nums[pos] != next_val:
        right_moving_pos += 1
        if right_moving_pos == N:
            break
    