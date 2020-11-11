from collections import deque


def solution(priorities, location):
    answer = 1
    max_p = max(priorities)
    indice = deque(list(range(len(priorities))))
    priorities = deque(priorities)
    while priorities:
        now_idx = indice.popleft()
        now_p = priorities.popleft()
        if now_p >= max_p:
            if now_idx == location:
                return answer
            else:
                max_p = max(priorities)
                answer += 1
        else:
            indice.append(now_idx)
            priorities.append(now_p)
