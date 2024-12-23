from lista_arranjo import Lista

def primos(lim: int) -> str:
    '''
    Encontra todos os números primos menores que *lim*.
    
    Exemplos:
    >>> primos(2)
    '[]'
    >>> primos(20)
    '[2, 3, 5, 7, 11, 13, 17, 19]'
    '''
    primos = Lista()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        
        while eh_primo and i < primos.tamanho:
            if n % primos.valores[i] == 0:
                eh_primo = False
            i = i + 1
            
        if eh_primo:
            primos.insere(i, n)
            
        n = n + 1
        
    return primos.str()