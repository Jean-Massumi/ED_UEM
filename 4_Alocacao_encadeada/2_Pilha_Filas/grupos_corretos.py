from pilha_arranjo import Pilha

def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> grupos_corretos('([{}])')
    True
    >>> grupos_corretos('[](){}')
    True
    >>> grupos_corretos('({)}')
    False
    >>> grupos_corretos('(2*[3*{5+2]})')
    False
    >>> grupos_corretos('([a]*{b-c}-[10])*({(4-2)/8})')
    True
    '''
    p = Pilha()
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] in '([{':
            p.empilha(expr[i])
        elif expr[i] in ')]}':
            if p.vazia() or not par(p.desempilha(), expr[i]):
                corretos = False
        i = i + 1
    return p.vazia() and corretos


def par(a: str, b: str) -> bool:
    return a == '(' and b == ')' or \
            a == '[' and b == ']' or \
            a == '{' and b == '}'
