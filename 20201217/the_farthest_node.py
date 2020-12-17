def solution(n, edge):
    graph = {i + 1: [] for i in range(n)}
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)

    q = [1]
    visit = {1}
    nxt_q = []
    while q:
        answer = len(nxt_q)
        nxt_q = []
        for p in q:
            for nxt_p in graph[p]:
                if nxt_p not in visit:
                    nxt_q.append(nxt_p)
                    visit.add(nxt_p)
        q = nxt_q
    return answer
