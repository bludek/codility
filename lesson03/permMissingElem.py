def solution(A):
    return missing(A, len(A))


def missing(A, n):
    xor_sum = 0
    for i in range(0, n):
        xor_sum ^= A[i] ^ (i + 1)
    return xor_sum ^ (n + 1)
