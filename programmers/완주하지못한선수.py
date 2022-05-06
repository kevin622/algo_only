def solution(participant, completion):
    p_dict = {}
    for p in participant:
        p_dict[p] = p_dict.get(p, 0) + 1
    for c in completion:
        p_dict[c] -= 1
    for p in p_dict:
        if p_dict[p]:
            return p