def solution(A):
    return unpair(A)


def unpair(A):
    result = 0
    for number in A:
        result ^= number
    return result