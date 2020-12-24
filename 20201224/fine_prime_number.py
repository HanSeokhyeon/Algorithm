def solution(n):
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    for i in range(2, n+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return sum(prime)
