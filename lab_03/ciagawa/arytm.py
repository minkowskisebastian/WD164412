def n(a1, r, n):
    return a1 + (n - 1) * r

def sn(a1, r, n):
    return (a1 + n(a1, r, n)) * n / 2