from collections import deque


def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        now_v = dq.popleft()
        cnt = 0
        for nxt_v in dq:
            cnt += 1
            if nxt_v < now_v:
                break
        answer.append(cnt)
    return answer
