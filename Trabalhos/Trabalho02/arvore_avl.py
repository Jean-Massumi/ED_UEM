from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore
    altura: int

Arvore = No | None


def busca(t: Arvore, val: int) -> bool:
    '''
    Devolve True se *val* está em *t*, False caso contrário.

    Exemplos

    >>> t = insere_arvore(None, 3)    
    >>> t = insere_arvore(t, 1)       
    >>> t = insere_arvore(t, 4)       
    >>> busca(t, 1)
    True
    >>> busca(t, 2)
    False

    Teste de propriedade
    
    >>> t = None
    >>> for val in range(0, 100, 2):
    ...     t = insere_arvore(t, val)  # Removido str()
    >>> for val in range(0, 100, 2):
    ...     assert busca(t, val) == True, f'{val} deveria estar na árvore!'
    >>> for val in range(1, 100, 2):
    ...     assert busca(t, val) == False, f'{val} não deveria estar na árvore!'
    '''
    
    if t is None:
        return False
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)


def insere_arvore(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da árvore AVL que é o resultado da inserção de *val* em
    *t*.

    Se *val* já está em *t*, devolve *t*.

    Exemplos

    >>> t = insere_arvore(None, 3)   
    >>> t = insere_arvore(t, 1)    
    >>> t = insere_arvore(t, 4)      
    >>> busca(t, 1)
    True
    >>> busca(t, 2)
    False

    Testes de propriedade

    Nós testes a seguir, várias árvores são criadas pela inserção de elementos
    e após cada inserção é verificada se a árvore mantém a propriedade da AVL.

    >>> # Inserção em ordem
    >>> t = None
    >>> for val in range(100):
    ...     t = insere_arvore(t, val)  # Removido str()
    ...     assert eh_avl(t) == True, 'deveria ser avl!'
    
    >>> # Inserção aleatória
    >>> import random
    >>> chaves = list(range(100))
    >>> random.shuffle(chaves)
    >>> t = None
    >>> for val in chaves:
    ...     t = insere_arvore(t, val)  # Removido str()
    ...     assert eh_avl(t) == True, 'deveria ser avl'
    '''
    
    if t is None:
        return No(None, val, None, 0)
    
    elif val < t.val:
        t.esq = insere_arvore(t.esq, val)
        t = rebalanceia_esq(t)
    
    elif val > t.val:
        t.dir = insere_arvore(t.dir, val)
        t = rebalanceia_dir(t)
    
    return t



def remove_arvore(t: Arvore, val: int) -> No:
    r'''
    Devolve a raiz da árvore AVL que é o resultado da remoção de *val* em *t*.

    Se *val* não está em *t*, devolve *t*.

    Se *t* só tem um nó e *val* está nesse nó, devolve None.

    Exemplos

    >>> t = insere_arvore(None, 7)  
    >>> t = insere_arvore(t, 4)    
    >>> t = insere_arvore(t, 2)    
    >>> busca(t, 2)
    True
    >>> t = remove_arvore(t, 2)
    >>> busca(t, 2)
    False

    Testes de propriedade

    Nos testes a seguir várias árvores são criadas, em seguida algumas chaves
    são removidas e a proprieade de AVL e o resultado de busca são verificados.

    >>> # Remoção em ordem
    >>> t = None
    >>> for val in range(100):
    ...     t = insere_arvore(t, val)
    >>> for val in range(100):
    ...     t = remove_arvore(t, val)
    ...     assert busca(t, val) == False, f'{val} não deveria estar na árvore!'
    ...     assert eh_avl(t) == True, 'deveria ser avl!'
    
    >>> # Remoção aleatória
    >>> import random
    >>> chaves = list(range(100))
    >>> random.shuffle(chaves)
    >>> t = None
    >>> for val in range(100):
    ...     t = insere_arvore(t, val)
    >>> for val in chaves:
    ...     t = remove_arvore(t, val)
    ...     assert busca(t, val) == False, f'{val} não deveria estar na árvore!'
    ...     assert eh_avl(t) == True, 'deveria ser avl!'
    '''
    if t is None:
        return None
    
    elif val < t.val:
        t.esq = remove_arvore(t.esq, val)
        
        if t.dir is not None:
            t = rebalanceia_dir(t)
            
        else:
            atualiza_altura(t)
            
        return t
    
    elif val > t.val:
        t.dir = remove_arvore(t.dir, val)
        
        if t.esq is not None:    
            t = rebalanceia_esq(t)  
        
        else:
            atualiza_altura(t)
            
        return t
    
    else:  # val == t.val
        if t.esq is None:
            # Se t.dir é None
            #  t     ->  None
            #
            # Se t.dir não é None
            # r           D
            #  \     ->  / \
            #   D       DE DD
            #  / \
            # DE DD
            return t.dir
        elif t.dir is None:
            #     r       r
            #    /   ->  / \
            #   E       EE ED
            #  / \
            # EE ED
            return t.esq
        else:
            # Tem os dois filhos
            #     r           r (val=max)
            #    / \    ->   / \
            #   E   D       E   D
            #  com         sem
            #  max         max
            m = maximo(t.esq)
            t.val = m
            t.esq = remove_arvore(t.esq, m)
            return rebalanceia_dir(t)



def altura(t: Arvore) -> int:
    '''
    Devolve a altura da árvore *t*.
    Devolve -1 se *t* é None.
    '''
    if t is None:
        return -1
    else:
        return t.altura
    

def atualiza_altura(no: No):
    '''
    Atualiza a altura do *no*.
    Requer que a altura de *no.esq* e *no.dir* este ja corretas.
    '''
    no.altura = 1 + max(altura(no.esq), altura(no.dir))


def rotaciona_esq(r: No) -> No:
    r'''
    Rotaciona a árvore com raiz *r* conforme o seguinte esquema:

         r              x
        / \            / \
       A   x    ->    r   C
          / \        / \
         B   C      A   B

    E devolve como nova raiz o nó que estava em *r.dir* quando a função foi
    chamada.

    Considerando que *r* é raiz de uma árvore AVL, então nas duas árvores
    A < r < B < x < C. Ou seja, a propriedade de ABB é preservada.

    O atributos altura dos nós da rotação são atualizados.

    Requer que *r.dir* não seja None.
    
    >>> # 1  2  3  4  5
    >>> A, r, B, x, C = _cria_nos('12345')
    >>> x.esq, x.dir, x.altura = B, C, 1
    >>> r.esq, r.dir, r.altura = A, x, 2
    >>> # Chama a função
    >>> nr = rotaciona_esq(r) 
    >>> # Verifica
    >>> nr is x
    True
    >>> x == No(r, '4', C, 2)
    True
    >>> r == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    '''
    
    assert r.dir is not None
    x = r.dir
    r.dir = x.esq
    x.esq = r
    atualiza_altura(r)
    atualiza_altura(x)
    
    return x

def rotaciona_dir(r: No) -> No:
    r'''
    Rotaciona a árvore com raiz *r* conforme o seguinte esquema:

           x               r            
          / \             / \          
         r   C    ->     A   x        
        / \                 / \        
       A   B               B   C      

    E devolve como nova raiz o nó que estava em *r.esq* quando a função foi
    chamada.

    Considerando que *x* é raiz de uma árvore AVL, então nas duas árvores
    A < r < B < x < C. Ou seja, a propriedade de ABB é preservada.

    O atributos altura dos nós da rotação são atualizados.

    Requer que *r.esq* não seja None.
    
    >>> # 1  2  3  4  5
    >>> A, r, B, x, C = _cria_nos('12345')
    >>> r.esq, r.dir, r.altura = A, B, 1
    >>> x.esq, x.dir, x.altura = r, C, 2
    >>> # Chama a função
    >>> nx = rotaciona_dir(x)
    >>> # Verifica
    >>> nx is r
    True
    >>> x == No(B, '4', C, 1)
    True
    >>> r == No(A, '2', x, 2)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    '''
    
    assert r.esq is not None
    x = r.esq
    r.esq = x.dir
    x.dir = r
    atualiza_altura(r)
    atualiza_altura(x)
    
    return x


def rebalanceia_esq(r: No) -> No:
    r'''
    Verifica o balanceamento de *r*, considerando o caso da subárvore a
    esquerda com maior altura, e faz o rebalanceamento e atualização das
    alturas se necessário. Devolve a raiz da árvore balanceada.

    Requer que *r.esq* não seja None.

    O balanceamento é feito de acordo com os seguintes casos:

    Caso 1 - esquerda-esquerda

           r  <- rotaciona_dir   x
         // \                  /   \
         x   D                y     r
       // \                  / \   / \
       y   C                A   B C   D
      / \
     A   B

    Testes

    >>> # Cria a árvore
    >>> #1 2  3  4  5  6  7
    >>> A, y, B, x, C, r, D = _cria_nos('1234567')
    >>> r.esq, r.dir = x, D
    >>> x.esq, x.dir = y, C
    >>> y.esq, y.dir = A, B
    >>> for n in [A, B, y, C, x, r, D]: atualiza_altura(n)
    
    >>> # Chama a função
    >>> nr = rebalanceia_esq(r)
    >>> # Verifica
    >>> nr is x
    True
    >>> x == No(y, '4', r, 2)
    True
    >>> r == No(C, '6', D, 1)
    True
    >>> y == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True


    # Caso 2 - esquerda-direita

    #                     r            r  <- rotaciona_dir   y
    #                   // \          / \                  /   \
    # rotaciona_esq ->  x   D        y   D                x     r
    #                 // \          / \                  / \   / \
    #                 A   y        x   C                A   B C   D
    #                    / \      / \
    #                   B   C    A   B


    # Testes

    >>> # Cria a árvore
    >>> # 1  2  3  4  5  6  7
    >>> A, x, B, y, C, r, D = _cria_nos('1234567')
    >>> r.esq, r.dir = x, D
    >>> x.esq, x.dir = A, y
    >>> y.esq, y.dir = B, C
    >>> for n in [A, B, y, A, x, D, r]: atualiza_altura(n)

    >>> # Chama a função
    >>> nr = rebalanceia_esq(r)
    >>> # Verifica
    >>> nr is y
    True
    >>> y == No(x, '4', r, 2)
    True
    >>> r == No(C, '6', D, 1)
    True
    >>> x == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True
    '''
    assert r.esq is not None
    
    if abs(altura(r.esq) - altura(r.dir)) == 2:
        #r está desbalaceada
        if altura(r.esq.esq) >= altura(r.esq.dir):
            #Caso Esquerda-Esquerda
            return rotaciona_dir(r)
        else:
            #Caso Esquerda-Direita
            assert altura(r.esq.dir) > altura(r.esq.esq)
            r.esq = rotaciona_esq(r.esq)
            return rotaciona_dir(r)
    else:
        #r está balanceada
        atualiza_altura(r)
        return r
    
    

def rebalanceia_dir(r: No) ->No:
    r'''
    Verifica o balanceamento de *r*, considerando o caso da subárvore a
    direita com maior altura, e faz o rebalanceamento e atualização das
    alturas se necessário. Devolve a raiz da árvore balanceada.

    Requer que *r.dir* não seja None.

    O balanceamento é feito de acordo com os seguintes casos:

    Caso 1 - direita-direita

           r  <- rotaciona_esq     x
          / \\                   /   \\
         A    x                 r      y
            /  \\             /  \    / \\
           B     y           A    B  C    D
                / \\
               C    D

    Exemplos
    >>> # Cria a árvore
    >>> # 1  2  3  4  5  6  7
    >>> D, y, C, x, B, r, A = _cria_nos('1234567')
    >>> r.esq, r.dir = A, x
    >>> x.esq, x.dir = B, y
    >>> y.esq, y.dir = C, D
    >>> for n in [D, C, y, B, x, A, r]: atualiza_altura(n)
    
    >>> # Chama a função
    >>> nr = rebalanceia_dir(r)
    >>> # Verifica
    >>> nr is x
    True
    >>> x == No(r, '4', y, 2)
    True
    >>> r == No(A, '6', B, 1)
    True
    >>> y == No(C, '2', D, 1)
    True
    >>> A == No(None, '7', None, 0)
    True
    >>> B == No(None, '5', None, 0)
    True
    >>> C == No(None, '3', None, 0)
    True
    >>> D == No(None, '1', None, 0)
    True

    #Caso 2 - direita-esquerda

    #       r                              r  <- rotaciona_dir    y
    #      / \\                           / \                   /   \\
    #     D   x    <- rotaciona_dir      D   y                 r     x
    #       //  \                           /  \              / \   / \\
    #      y     A                         B    x            D   B C    A   
    #     / \                                  / \                
    #    B   C                                C   A              

    Exemplos
    >>> # Cria a árvore
    >>> #1 2  3  4  5  6  7
    >>> D, x, C, y, B, r, A = _cria_nos('1234567')
    >>> y.esq, y.dir = B, C
    >>> x.esq, x.dir = y, A
    >>> r.esq, r.dir = D, x
    >>> for n in [D, C, y, B, x, A, r]: atualiza_altura(n)
    
    >>> # Chama a função
    >>> nr = rebalanceia_dir(r)
    >>> # Verifica
    >>> nr is y
    True
    >>> y == No(r, '4', x, 2)
    True
    >>> r == No(D, '6', B, 1)
    True
    >>> x == No(C, '2', A, 1)
    True
    >>> A == No(None, '7', None, 0)
    True
    >>> B == No(None, '5', None, 0)
    True
    >>> C == No(None, '3', None, 0)
    True
    >>> D == No(None, '1', None, 0)
    True
    '''
    assert r.dir is not None

    
    if abs(altura(r.dir) - altura(r.esq)) == 2:
        #r está desbalaceada
        if altura(r.dir.dir) >= altura(r.dir.esq):
            #Caso Direita-Direita
            return rotaciona_esq(r)
        else:
            #Caso Direita-Esquerda
            assert altura(r.dir.esq) > altura(r.dir.dir)
            r.dir = rotaciona_dir(r.dir)
            return rotaciona_esq(r)
    else:
        #r estábalaceada
        atualiza_altura(r)
        return r



def maximo(no: No) -> int:
    '''
    Encontra o valor máximo em *no*.

    Exemplos

    >>> no = None
    >>> for val in [5, 1, 2, 7, 6, 3, 8, 4]:
    ...     no = insere_arvore(no, val)
    >>> maximo(no)
    8
    '''
    while no.dir is not None:
        no = no.dir
    return no.val


def _cria_nos(valores: int) -> list[No]:
    # Cria uma lista de nós com cada caractere de *chaves* sendo uma chave.
    # Esta função é utilizada para simplificar a criação dos testes.
    nos = []
    for val in valores:
        nos.append(No(None, val, None, 0))
    return nos


# Funções de verificação
#
# A função eh_avl é utilizada para os testes aleatórios de inserção e remoção.

def eh_avl(r: Arvore) -> bool:
    return eh_abb(r) and eh_balanceada(r) and altura_correta(r)


def eh_abb(r: Arvore) -> bool:
    return r is None or \
        (r.esq is None or r.esq.val < r.val and eh_abb(r.esq)) and \
        (r.dir is None or r.val < r.dir.val and eh_abb(r.dir))


def eh_balanceada(r: Arvore) -> bool:
    return r is None or \
        abs(altura(r.esq) - altura(r.dir)) <= 1 and \
        eh_balanceada(r.esq) and \
        eh_balanceada(r.dir)


def altura_correta(r: Arvore) -> bool:
    return r is None or \
        r.altura == 1 + max(altura(r.esq), altura(r.dir)) and \
        altura_correta(r.esq) and \
        altura_correta(r.dir)


