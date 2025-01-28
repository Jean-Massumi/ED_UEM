def n_string(palavra: str, n: int) -> str:
    '''
    Devolva uma nova string repetindo a *palavra* *n* vezes.
    
    Exemplo
    >>> n_string("mouse", 2)
    'mousemouse'
    >>> n_string("casa", 0)
    ''
    >>> n_string("pá", 1)
    'pá'
    '''
    
    if n == 0:
        return ''
    
    else:
        if n == 1:
            return palavra
        
        else:
            return palavra + (n_string(palavra, n - 1))
    
