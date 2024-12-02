from pilha_arranjo import Pilha

def avalia_posfixa(lst: list[str]) -> int:
    '''
    Avalia e calcula uma expressão posfixa e devolva o seu resultado.
    
    A análise da expressão começa da esquerda para a direita.
    
    Se o valor for um operando, empilhe em uma pilha.
    Se o valor for um operador, desempilhe dois valores da pilha e calcule o seu o resultado
    e depois devolva o valor resultante para a pilha.
    
    Obs: A expressão fornecida é válida e bem formatada, ou seja, não há operadores sem 
    operandos suficientes, e todos os tokens são ou números ou operadores válidos.
    
    Exemplos
    >>> avalia_posfixa(['102'])
    102
    >>> avalia_posfixa(['55', '5', '/'])
    11
    >>> avalia_posfixa(['5', '6', '*', '3', '+'])
    33
    >>> avalia_posfixa(['5', '-6', '*', '3', '+', '10', '-'])
    -37
    '''
    
    p = Pilha()
    
    for valor in lst:
        if valor in "+-/*":
            operando1 = int(p.desempilha())
            operando2 = int(p.desempilha())
            
            if valor == '+':
                resultado = operando2 + operando1
                
            elif valor == '-':
                resultado = operando2 - operando1
                
            elif valor == '/':
                resultado = operando2 // operando1
                
            else:
                resultado = operando2 * operando1

            p.empilha(str(resultado))
            
        else:
            p.empilha(valor)
            
    return int(p.desempilha())