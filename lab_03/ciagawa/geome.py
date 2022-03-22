def n(a1, q, n):
    return a1 * q ** (n - 1)

def sn(a1, q, n):
    return a1 * (1 - q ** n) / (1 - q)
