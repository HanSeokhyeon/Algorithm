def solution(n):
    def convert_3(num):
        note = '012'
        q, r = divmod(num, 3)
        w = note[r]
        return convert_3(q) + w if q else w

    n_3 = convert_3(n)
    answer = 0
    for i, v in enumerate(n_3):
        answer += 3 ** i * int(v)
    return answer
