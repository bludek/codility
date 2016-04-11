def solution(S, P, Q):
    return dna(S, P, Q)


def dna(S, P, Q):
    n = len(S)
    m = len(P)
    result = [0] * m
    A = [0] * (n + 1)
    T = [0] * (n + 1)
    C = [0] * (n + 1)
    G = [0] * (n + 1)

    for i in range(0, n):
        if i + 1 <= n:
            A[i + 1] = A[i]
            T[i + 1] = T[i]
            C[i + 1] = C[i]
            G[i + 1] = G[i]
        if S[i] == 'A':
            A[i + 1] += 1
        if S[i] == 'T':
            T[i + 1] += 1
        if S[i] == 'C':
            C[i + 1] += 1
        if S[i] == 'G':
            G[i + 1] += 1

    for i in range(0, m):
        containsA = A[Q[i] + 1] - A[P[i]]
        containsT = T[Q[i] + 1] - T[P[i]]
        containsC = C[Q[i] + 1] - C[P[i]]
        containsG = G[Q[i] + 1] - G[P[i]]
        if containsA > 0:
            result[i] = 1
        elif containsC > 0:
            result[i] = 2
        elif containsG > 0:
            result[i] = 3
        elif containsT > 0:
            result[i] = 4
    return result
