def solution(X, Y, D):
    return jump(X, Y, D)


def jump(X, Y, D):
    diff = Y - X
    return diff // D + (diff % D > 0)