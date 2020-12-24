def solution(s, n):
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    answer = []
    for c in s:
        if c.isupper():
            idx = up.index(c) + n
            if idx >= 26:
                idx -= 26
            answer.append(up[idx])
        elif c.islower():
            idx = low.index(c) + n
            if idx >= 26:
                idx -= 26
            answer.append(low[idx])
        else:
            answer.append(" ")
    return "".join(answer)
