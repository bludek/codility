def solution(A):
    return max_product(A, len(A))


def max_product(A, n):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])