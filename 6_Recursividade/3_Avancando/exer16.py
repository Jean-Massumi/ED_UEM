def divisores(n: int, x: int) -> list[int]:
    '''
    Devolva uma lista com todos os divisores de *n* menores ou iguaisque *x*.
    x <= n
    
    Exemplo
    >>> divisores(16, 7)
    [1, 2, 4]
    >>> divisores(37, 37)
    [1, 37]
    >>> divisores(63, 16)
    [1, 3, 7, 9]
    '''

    if x == 0:
        return []
    
    else:
        lst = divisores(n, x - 1)
        if n % x == 0:
            lst.append(x)
            
    return lst
