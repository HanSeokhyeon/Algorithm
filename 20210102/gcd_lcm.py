from math import gcd


def solution(n, m):
    answer = gcd(n, m)
    return answer, n*m // answer
