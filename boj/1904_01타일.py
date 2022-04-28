import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
else:
    a = 1
    b = 2
    for _ in range(3, N + 1):
        b, a = (a + b) % 15746, b
    print(b)
