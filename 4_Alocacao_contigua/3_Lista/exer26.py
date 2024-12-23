from lista_arranjo import Lista

def remove_elem_cons(lista: Lista) -> None:
    '''
    Remove todas as ocorrências de elementos iguais consecutivos.
    
    Exemplo
    >>> lst = Lista()
    >>> lst.insere(0, 3)
    >>> lst.insere(0, 3)
    >>> lst.insere(0, 3)
    >>> lst.insere(3, 1)
    >>> lst.insere(4, 5)
    >>> lst.insere(5, 5)
    >>> lst.str()
    '[3, 3, 3, 1, 5, 5]'
    >>> remove_elem_cons(lst)
    >>> lst.str()
    '[3, 1, 5]'
    '''

    numero = lista.valores[0]
    cont = 1
    
    for i in range(1, lista.tamanho):
        if (lista.valores[i] != numero):
            numero = lista.valores[i]
            lista.valores[cont] = numero
            
            cont += 1
        
        else:
            lista.tamanho -= 1


