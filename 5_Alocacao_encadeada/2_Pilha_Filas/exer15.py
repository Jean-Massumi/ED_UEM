from exer14 import Pilha

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
    
    for char in expr:
        if char in  "([{":
            p.empilha(char)
            
        elif char in "}])":
            topo = p.desempilha()
            
            if topo is None or not par(topo, char):
                return False
            
    return p.vazia()
    

def par(a: str, b: str) -> bool:
    return a == '(' and b == ')' or \
            a == '[' and b == ']' or \
            a == '{' and b == '}'


# Eu prefiro a versão com a pilha encadeada, pois o uso do 
# None torna o código mais simples e fácil de entender.
