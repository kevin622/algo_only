N = int(input())
order = []


def hanoi(n, before, after):
    if n == 1:
        order.append((before, after))
        return 1
    else:
        middle = list({1, 2, 3} - {before, after})[0]
        return hanoi(n - 1, before, middle) + hanoi(1, before, after) + hanoi(n - 1, middle, after)


answer = hanoi(N, 1, 3)
print(answer)
for a, b in order:
    print(a, b)
