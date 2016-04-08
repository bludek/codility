def solution(A, K):
    return shift(A, K)


def shift(seq, n):
    if len(seq) == 0:
        return seq
    n = n % len(seq)
    return seq[-n:] + seq[:-n]
