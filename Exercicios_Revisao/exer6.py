def modifica_string(texto : str, n : int) -> str:
    """
    Modifica a string *texto* de forma que tenha exatamente *n* caracteres.

    - Se o comprimento de *texto* for maior que *n*, os caracteres excedentes são removidos do final.
    - Se o comprimento de *texto* for menor que *n*, espaços em branco são adicionados ao final para atingir o comprimento *n*.
    - Se o comprimento de *texto* for igual a *n*, a string é retornada inalterada.

    Parâmetros:
    - texto (str): A string de entrada que será modificada.
    - n (int): O número exato de caracteres que a string modificada deve conter.

    Retorno:
    - str: A string modificada com o comprimento exatamente igual a *n*.
    
    Exemplos:
    >>> modifica_string("Paralelismo", 5)
    'Paral'
    >>> modifica_string("Paralelismo", 11)
    'Paralelismo'
    >>> modifica_string("Paralelismo", 15)
    'Paralelismo    '
    >>> modifica_string("", 10)
    '          '
    """
    
    if len(texto) > n:
        modificado = texto[:n]
    
    elif len(texto) < n:
        modificado = texto + " " * (n - len(texto))
        
    else:
        modificado = texto
        
    return modificado