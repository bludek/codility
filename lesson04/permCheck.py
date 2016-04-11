def solution(A):
    return permutation(A, len(A))


def permutation(A, n):
    cover = [-1] * (n)
    uncover = n

    for i in range(0, n):
        if A[i] > n:
            return 0
        elif cover[A[i] - 1] != -1:
            return 0
        else:
            cover[A[i] - 1] = i
            uncover -= 1
            if uncover == 0:
                return  1
    return 0
