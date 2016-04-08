def solution(A):
    return equi(A, len(A))


def equi(A, n):
    if n == 0:
        return -1

    sum_right = sum(A)
    sum_left = 0
    for i in range(0, n):
        if sum_right - A[i] == sum_left:
            return i
        else:
            sum_left += A[i]
            sum_right -= A[i]
    return -1
