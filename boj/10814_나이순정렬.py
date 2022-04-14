import sys
input = sys.stdin.readline
N = int(input())
arr = [input().rstrip().split(' ') for _ in range(N)]
arr = list(enumerate(map(lambda x: [int(x[0]), x[1]], arr)))
arr.sort(key=lambda x: (x[1][0], x[0]))
for _, a in arr:
    print(*a)
