import sys

arr = list(map(int, sys.stdin.readline().split()))
used = [0] * 8
x_coors = [0.] * 8
y_coors = [0.] * 8
answer = 0


def check_rotation(x1, y1, x2, y2, x3, y3):
    determinant: float = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)
    if determinant < 0:
        return 'clockwise'


def perm(depth=0):
    global answer
    if depth == 8:
        val = 1
        for j in range(8):
            x1, y1 = x_coors[j], y_coors[j]
            x2, y2 = x_coors[(j + 1) % 8], y_coors[(j + 1) % 8]
            x3, y3 = x_coors[(j + 2) % 8], y_coors[(j + 2) % 8]
            if check_rotation(x1, y1, x2, y2, x3, y3) == 'clockwise':
                continue
            else:
                val = 0
                break
        answer += val
        return
    for i in range(8):
        used[i] = 1
        perm(depth + 1)
        used[i] = 0


perm()
print(answer)
