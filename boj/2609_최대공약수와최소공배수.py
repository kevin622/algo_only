# 유클리드 호제법이래(웅성웅성)
def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
max_div = gcd(a, b)
min_mul = a * b // max_div
print(max_div)
print(min_mul)
