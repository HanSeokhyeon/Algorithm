def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        answer.append([])
        for b1, b2 in zip(a1, a2):
            answer[-1].append(b1+b2)
    return answer
