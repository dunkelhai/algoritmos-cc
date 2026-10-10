"""Maior subsequência comum entre duas strings."""


def lcs(a, b):
    """Retorna uma maior subsequência comum de `a` e `b`."""
    m, n = len(a), len(b)
    t = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            t[i + 1][j + 1] = t[i][j] + 1 if a[i] == b[j] else max(t[i][j + 1], t[i + 1][j])
    resultado = []
    i, j = m, n
    while i and j:
        if a[i - 1] == b[j - 1]:
            resultado.append(a[i - 1])
            i -= 1
            j -= 1
        elif t[i - 1][j] >= t[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(resultado))
