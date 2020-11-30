def solution(p):
    def is_correct(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
        return not stack

    def detatch(s):
        left, right = 0, 0
        u = ""
        for i, c in enumerate(s):
            u += c
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                break
        v = s[len(u):]
        return u, v

    def reverse(s):
        return "".join([')' if c == '(' else '(' for c in s])

    def recursive(s):
        if s == '':
            return ''
        u, v = detatch(s)
        if is_correct(u):
            return u + recursive(v)
        else:
            return '(' + recursive(v) + ')' + reverse(u[1:-1])

    return p if is_correct(p) else recursive(p)
