def solution(A):
    return diff(A)


def diff(A):
    head = A[0]
    tail = sum(A[1:])
    minDiff = abs(head - tail)

    for i in range(1, len(A) - 1):
        head += A[i]
        tail -= A[i]
        if abs(head - tail) < minDiff:
            minDiff = abs(head - tail)

    return minDiff