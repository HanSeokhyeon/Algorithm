def solution(operations):
    q = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            q.append(num)
            q.sort()
        elif q:
            if num == 1:
                q.pop()
            else:
                q.pop(0)
    if q:
        return [q[-1], q[0]]
    else:
        return [0, 0]
