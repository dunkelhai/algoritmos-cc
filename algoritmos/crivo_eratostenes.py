"""Números primos até n pelo crivo de Eratóstenes."""


def primos_ate(n):
    if n < 2:
        return []
    eh_primo = [True] * (n + 1)
    eh_primo[0] = eh_primo[1] = False
    i = 2
    while i * i <= n:
        if eh_primo[i]:
            for m in range(i * i, n + 1, i):
                eh_primo[m] = False
        i += 1
    return [i for i, p in enumerate(eh_primo) if p]
