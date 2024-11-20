from pilha_arranjo import Pilha

def inverte_string(palavra: str) -> str:
    """
    Inverte os caracteres da *palavra*.
    
    Exemplo:
    >>> inverte_string("Casa")
    'asaC'
    >>> inverte_string("subi no onibus")
    'subino on ibus'
    >>> inverte_string("aranha")
    'ahnara'
    """
    p = Pilha()
    
    for caractere in palavra:
        p.empilha(caractere)
    
    palavra_invertida = ""
    
    while not (p.vazia()):
        palavra_invertida += p.desempilha()

    return palavra_invertida

