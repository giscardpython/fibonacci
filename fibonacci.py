def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci_recursive(n - 1)
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
        return sequencia


n = int(input('Informe um número inteiro: '))

print(f'Fibonaaci Resursivo de {n}: {fibonacci_recursive(n)}')

