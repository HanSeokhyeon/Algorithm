def solution(arr, divisor):
    answer = []
    for v in arr:
        if v % divisor == 0:
            answer.append(v)
    if answer:
        return sorted(answer)
    else:
        return [-1]
