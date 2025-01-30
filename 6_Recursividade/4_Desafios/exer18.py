def ordena_crescente(lst: list[int]) -> None:
    '''
    Modicaca a lista de números, ordenando em ordem não decrescente.
    
    Exemplos
    >>> lst = [1, 2, 3, 4]
    >>> lst1 = [4, 3, 2, 1]
    >>> lst2 = [1, 4, 2, 3]
    >>> lst3 = [3, 4, 2, 1]
    >>> ordena_crescente(lst)
    >>> ordena_crescente(lst1)
    >>> ordena_crescente(lst2)
    >>> ordena_crescente(lst3)
    >>> lst
    [1, 2, 3, 4]
    >>> lst1
    [1, 2, 3, 4]
    >>> lst2
    [1, 2, 3, 4]
    >>> lst3
    [1, 2, 3, 4]
    '''

    if len(lst) > 1:
        
        m = len(lst) // 2
        dir = lst[:m]
        esq = lst[m:]
        
        ordena_crescente(dir)
        ordena_crescente(esq)
        
        intercala(lst, dir, esq)
        
        
def intercala(lst: list[int], dir: list[int], esq: list[int]):
    assert len(lst) == len(dir) + len(esq)
    
    i, j , k = 0, 0, 0
    
    while i < len(dir) and j < len(esq):
        if dir[i] <= esq[j]:
            lst[k] = dir[i]
            i += 1
            
        else:
            lst[k] = esq[j]
            j += 1
            
        k += 1
        
    while i < len(dir):
        lst[k] = dir[i]
        i += 1
        k += 1
        
    while j < len(esq):
        lst[k] = esq[j]
        j += 1
        k += 1





