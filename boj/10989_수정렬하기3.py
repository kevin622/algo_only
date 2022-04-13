import sys

input = sys.stdin.readline

N = int(input())
count = [0] * 10001
for _ in range(N):
    num = int(input())
    count[num] += 1
for i in range(len(count)):
    if count[i]:
        sys.stdout.write((str(i) + '\n') * count[i])
