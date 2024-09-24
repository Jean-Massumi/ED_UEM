def sem_espacos_extras(frase : str) -> bool:
    """
    Verifica se uma *frase* atende à regra "sem espaços extras", ou seja, 
    o texto não deve começar nem terminar com espaços em branco.
    
    Devolve *False* se *frase* não atender a regra. Caso contrário *True*
    
    Exemplos:
    >>> sem_espacos_extras(" Olá mundo")
    True
    >>> sem_espacos_extras(" Amo programar ")
    False
    >>> sem_espacos_extras("Eis a questão! ")
    True
    >>> sem_espacos_extras("Anime")
    True
    >>> sem_espacos_extras("")
    True
    """
    
    if (frase == "") or (frase[0] != " " or frase[-1] != " "):
        regra = True
    
    else:
        regra = False
                
    return regra