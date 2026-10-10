"""Fibonacci: iterativo e por exponenciação de matrizes."""


def fibonacci(n):
    if n < 0:
        raise ValueError("n deve ser não negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_matriz(n):
    """O(log n) usando [[1,1],[1,0]]^n."""
    def mult(x, y):
        return [
            [x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]],
            [x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]],
        ]

    resultado, base = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    while n > 0:
        if n & 1:
            resultado = mult(resultado, base)
        base = mult(base, base)
        n >>= 1
    return resultado[0][1]
