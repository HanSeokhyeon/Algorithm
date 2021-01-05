def solution(num):
    def recursive(n, cnt):
        if cnt > 500:
            return -1
        if n == 1:
            return cnt
        elif n%2:
            return recursive(3*n+1, cnt+1)
        else:
            return recursive(n/2, cnt+1)
    return recursive(num, 0)
