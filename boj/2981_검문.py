import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
new_arr = []
for i in range(1, len(arr)):
    new_arr.append(arr[i] - arr[i - 1])

new_arr = list(set(new_arr))


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


while len(new_arr) > 1:
    a = new_arr.pop()
    b = new_arr.pop()
    new_arr.append(gcd(a, b))

n = new_arr[0]
answers = []
for i in range(2, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        if (i ** 2) == n:
            answers.append(i)
        else:
            answers.extend([i, n // i])
answers.append(n)
answers.sort()
print(*answers)
