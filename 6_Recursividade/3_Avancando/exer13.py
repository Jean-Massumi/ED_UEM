def impar(n: int) -> bool:
    '''
    Devolve True se *n* é um número ímpar, False caso contrário.

    Exemplos
    >>> impar(27)
    True
    >>> impar(44)
    False
    '''

    if n < 0:
        return impar(-n)

    else:
        if n == 0:
            return False
        
        else:
            return par(n - 1)
    
    
def par(n: int) -> bool:
    '''
    Devolve True se *n* é número par, False caso contrário.

    Exemplos
    >>> par(12)
    True
    >>> par(17)
    False
    '''
    
    if n < 0:
        return par(-n)

    else:
        if n == 0:
            return True

        else:
            return impar(n - 1)


