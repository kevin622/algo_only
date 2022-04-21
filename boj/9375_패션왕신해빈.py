T = int(input())
for tc in range(T):
    n = int(input())
    clothe_dict = {}
    for _ in range(n):
        name, cat = input().split()
        clothe_dict[cat] = clothe_dict.get(cat, []) + [name]
    answer = 1
    for key in clothe_dict:
        answer *= len(clothe_dict[key]) + 1
    print(answer - 1)
