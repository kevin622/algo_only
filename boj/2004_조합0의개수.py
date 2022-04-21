import sys

input = sys.stdin.readline


def get_2_cnt(n: int):
    i = 2
    answer = 0
    while n >= i:
        answer += n // i
        i *= 2
    return answer


def get_5_cnt(n: int):
    i = 5
    answer = 0
    while n >= i:
        answer += n // i
        i *= 5
    return answer


n, m = map(int, input().split())
n_5_cnt = get_5_cnt(n)
n_2_cnt = get_2_cnt(n)
m_5_cnt = get_5_cnt(m)
m_2_cnt = get_2_cnt(m)
n_m_5_cnt = get_5_cnt(n - m)
n_m_2_cnt = get_2_cnt(n - m)
cnt_5 = n_5_cnt - (m_5_cnt + n_m_5_cnt)
cnt_2 = n_2_cnt - (m_2_cnt + n_m_2_cnt)
print(min(cnt_2, cnt_5))
