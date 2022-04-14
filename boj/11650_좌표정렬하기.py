import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))
print('\n'.join(map(lambda x: (str(x[0]) + ' ' + str(x[1])), arr)))
