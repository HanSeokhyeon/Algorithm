import heapq


def solution(jobs):
    answer, now, last, count = 0, 0, -1, 0
    hq = []
    while count < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                answer += now - job[0]
                heapq.heappush(hq, job[1])
        if hq:
            answer += len(hq) * hq[0]
            last = now
            now += heapq.heappop(hq)
            count += 1
        else:
            now += 1
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
print(solution([[0, 3], [4, 3], [7, 3]]))  # 3
print(solution([[0, 1], [0, 2], [0, 3]]))  # 3
print(solution([[0, 9], [2, 6], [3, 3]]))  # 11
print(solution([[0, 3], [2, 4], [2, 3]]))  # 5
