def solution(arr):
    answer = [arr[0]]
    before = arr[0]
    for v in arr:
        if v != before:
            answer.append(v)
        before = v
    return answer
