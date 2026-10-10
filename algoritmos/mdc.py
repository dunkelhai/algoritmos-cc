"""Algoritmo de Euclides e variações."""


def mdc(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def mmc(a, b):
    return 0 if a == 0 or b == 0 else abs(a * b) // mdc(a, b)


def euclides_estendido(a, b):
    """Retorna (g, x, y) com a·x + b·y = g = mdc(a, b)."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inverso_modular(a, m):
    g, x, _ = euclides_estendido(a, m)
    if g != 1:
        raise ValueError("inverso não existe")
    return x % m
