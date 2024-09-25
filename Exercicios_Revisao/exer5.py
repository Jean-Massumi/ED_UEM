def determina_sinal_numero(numero : int) -> int:
    """
    Verifica se o *numero* é positivo, negativo ou neutro.
    
    Se for positivo, devolva 1;
    Se for negativo, devolva -1;
    Se for 0, devolva 0;
    
    Exemplos:
    >>> determina_sinal_numero(177)
    1
    >>> determina_sinal_numero(-88)
    -1
    >>> determina_sinal_numero(0)
    0
    >>> determina_sinal_numero(-1.98)
    -1
    >>> determina_sinal_numero(25.8)
    1
    """
    
    if numero > 0:
        sinal = 1    
    
    elif numero < 0:
        sinal = -1
        
    else:
        sinal = 0
    
    return sinal