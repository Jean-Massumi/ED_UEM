from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore
    altura: int

Arvore = No | None

def _cria_nos(chaves: str) -> list[No]:
    # Cria uma lista de nós com cada caractere de chaves sendo uma chave.
    # Esta função é utilizada para simplificar a criação dos testes.
    nos = []
    for chave in chaves:
        nos.append(No(None, chave, None))
    return nos


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
    Rotaciona a árvore com raiz *r*
    conforme o seguinte esquema:
    
        r       x
        /\      /\
       A  x -> r  C
         /\   /\
        B  C A  B

    E devolve como nova raiz o nó que estava
    em *r.dir* quando a função foi chamada.
    
    Requer que *r.dir* não seja None.
    
    # >>> # 1  2  3  4  5
    # >>> A, r, B, x, C = _cria_nos('12345')
    # >>> x.esq, x.dir, x.altura = B, C, 1
    # >>> r.esq, r.dir, r.altura = A, x, 2
    # >>> # Chama a função
    # >>> nr = rotaciona_esq(r)
    # >>> # Verifica
    # >>> nr is x
    # True
    # >>> x == No(r, '4', C, 2)
    # True
    # >>> r == No(A, '2', B, 1)
    # True
    # >>> A == No(None, '1', None, 0)
    # True
    # >>> B == No(None, '3', None, 0)
    # True
    # >>> C == No(None, '5', None, 0)
    # True
    
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
    Rotaciona a árvore com raiz *r*
    conforme o seguinte esquema:
    
        r       x
        /\      /\
       A  x -> r  C
         /\   /\
        B  C A  B

    E devolve como nova raiz o nó que estava
    em *r.dir* quando a função foi chamada.
    
    Requer que *r.dir* não seja None.
    
    # >>> # 1  2  3  4  5
    # >>> A, r, B, x, C = _cria_nos('12345')
    # >>> x.esq, x.dir, x.altura = B, C, 1
    # >>> r.esq, r.dir, r.altura = A, x, 2
    # >>> # Chama a função
    # >>> nr = rotaciona_dir(r)
    # >>> # Verifica
    # >>> nr is x
    # True
    # >>> x == No(r, '4', C, 2)
    # True
    # >>> r == No(A, '2', B, 1)
    # True
    # >>> A == No(None, '1', None, 0)
    # True
    # >>> B == No(None, '3', None, 0)
    # True
    # >>> C == No(None, '5', None, 0)
    # True
    
    '''
    
    assert r.esq is not None
    x = r.esq
    r.esq = x.dir
    x.dir = r
    atualiza_altura(r)
    atualiza_altura(x)
    
    return x


def rebalanceia_esq(r: No) -> No:
    '''
    Verifica o balanceamento de *r*,considerando o caso da sub árvoreaes quer da com maior altura,
    e faz o rebalanceamento e atualização das alturas se necessário. Devolve a raiz da árvore balanceada.
    '''
    assert r.esq is not None
    if altura(r.esq) - altura(r.dir) == 2:
        #r está desbalaceada
        if altura(r.esq.esq) > altura(r.esq.dir):
            #Caso Esquerda-Esquerda
            return rotaciona_dir(r)
        else:
            #Caso Esquerda-Direita
            assert altura(r.esq.dir) > altura(r.esq.esq)
            r.esq = rotaciona_esq(r.esq)
            return rotaciona_dir(r)
    else:
        #r estábalaceada
        atualiza_altura(r)
        return r
    
    

def rebalanceia_dir(r: No) ->No:
    ''' 
    Verifica o balanceamento de *r*,considerando o caso da sub árvoreaes quer da com maior altura,
    e faz o rebalanceamento e atualização das alturas se necessário. Devolve a raiz da árvore balanceada.
    '''
    assert r.dir is not None
    if altura(r.dir) - altura(r.esq) == 2:
        #r está desbalaceada
        if altura(r.dir.dir) > altura(r.dir.esq):
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


def insere_arvore(t: Arvore, val: int) -> No:
    if t is None:
        return No(None, val, None, 0)
    
    else:
        if val < t.val:
            t.esq =insere_arvore(t.esq,val)
            t = rebalanceia_esq(t)
        
        elif val > t.val:
            t.dir =insere_arvore(t.dir,val)
            t = rebalanceia_dir(t)
        
        else:#val==t.val
            pass
        return t


def remove_arvore(t: Arvore, val: int) -> No:
    r'''
    Devolve a raiz da árvore AVL que é o resultado da remoção de *chave* em *r*.

    Se *chave* não está em *r*, devolve *r*.

    Se *r* só tem um nó e *chave* está nesse nó, devolve None.

    Exemplos

    # >>> r = insere(None, 'g')
    # >>> r = insere(r, 'd')
    # >>> r = insere(r, 'b')
    # >>> busca(r, 'b')
    # True
    # >>> r = remove(r, 'b')
    # >>> busca(r, 'b')
    # False


    Testes de propriedade

    Nos testes a seguir várias árvores são criadas, em seguida algumas chaves
    são removidas e a proprieade de AVL e o resultado de busca são verificados.

    # >>> # Remoção em ordem
    # >>> r = None
    # >>> for chave in range(100):
    # ...     r = insere(r, str(chave))
    # >>> for chave in range(100):
    # ...     r = remove(r, str(chave))
    # ...     assert busca(r, str(chave)) == False, f'{chave} não deveria estar na árvore!'
    # ...     assert eh_avl(r) == True, 'deveria ser avl!'
    # >>> # Remoção aleatória
    # >>> import random
    # >>> chaves = list(range(100))
    # >>> random.shuffle(chaves)
    # >>> r = None
    # >>> for chave in range(100):
    # ...     r = insere(r, str(chave))
    # >>> for chave in chaves:
    # ...     r = remove(r, str(chave))
    # ...     assert busca(r, str(chave)) == False, f'{chave} não deveria estar na árvore!'
    # ...     assert eh_avl(r) == True, 'deveria ser avl!'
    '''
    if t is None:
        return None
    
    elif val < t.val:
        t.esq = remove_arvore(t.esq, val)
        t = rebalanceia_esq(t)
        
        return t
    elif val > t.val:
        t.dir = remove_arvore(t.dir, val)
        t = rebalanceia_dir(t)  
        
        return t
    
    else:  # chave == t.chave
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
            #     r           r (chave=max)
            #    / \    ->   / \
            #   E   D       E   D
            #  com         sem
            #  max         max
            m = maximo(t.esq)
            t.chave = m
            t.esq = remove_arvore(t.esq, m)
            return t


def maximo(no: No) -> int:
    '''
    Encontra o valor máximo em *r*.

    Exemplos

    # >>> r = None
    # >>> for val in [5, 1, 2, 7, 6, 3, 8, 4]:
    # ...     r = insere(r, val)
    # >>> maximo(r)
    # 8
    '''
    while no.dir is not None:
        no = no.dir
    return no.val



class Conjunto:
    '''
    Uma coleção de números inteiros distintos.

    Exemplos

    # >>> c1 = Conjunto()
    # >>> c1.insere(10)
    # >>> c1.insere(3)
    # >>> c1.insere(12)
    # >>> c1.insere(7)
    # >>> c1.em_ordem()
    # [3, 7, 10, 12]
    # >>> c2 = Conjunto()
    # >>> c2.insere(20)
    # >>> c2.insere(3)
    # >>> c2.insere(1)
    # >>> c2.insere(10)
    # >>> c2.em_ordem
    # [1, 3, 10, 20]
    # >>> c1.intersecao(c2).em_ordem()
    # [3, 7]
    # >>> c1.remove(12)
    # >>> c2.remove(12)
    # >>> c1.uniao(c2).em_ordem()
    # [1, 3, 7, 10, 20]
    '''
    
    arvore_conjunto: Arvore

    def __init__(self) -> None:
        '''Cria um novo conjunto vazio'''
        
        self.arvore_conjunto = None


    def insere(self, valor: int) -> None:
        '''
        Insere *valor* no conjunto
        
        Exemplos:
        >>> c = Conjunto()
        >>> c.insere(6)
        >>> c.insere(10)
        >>> c.insere(13)
        >>> c.arvore_conjunto.val
        10
        >>> c.arvore_conjunto.esq.val
        6
        >>> c.arvore_conjunto.dir.val
        13
    
        '''
        
        self.arvore_conjunto = insere_arvore(self.arvore_conjunto , valor)

    def remove(self, valor: int) -> None:
        '''Remove o *valor* do conjunto, se ele estiver presente.'''

        self.arvore_conjunto = remove_arvore(self.arvore_conjunto, valor)  


    def intersecao(self, outro: Conjunto) -> Conjunto:
        '''Cria um novo conjunto com os elementos que *self* e *outro* têm em comum.'''


    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Cria um novo conjunto com os elementos de *self* e *outro*.'''



    def em_ordem(self) -> list[int]:
        '''Devolve uma lista com os elemento do conjunto em ordem.'''