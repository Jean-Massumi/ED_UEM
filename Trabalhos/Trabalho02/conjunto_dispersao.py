from __future__ import annotations


class Conjunto:
    '''
    Uma coleção de números inteiros distintos.

    Exemplos

    >>> c1 = Conjunto()
    >>> c1.insere(10)
    >>> c1.insere(3)
    >>> c1.insere(12)
    >>> c1.insere(7)
    >>> c1.em_ordem()
    [3, 7, 10, 12]
    >>> c2 = Conjunto()
    >>> c2.insere(20)
    >>> c2.insere(3)
    >>> c2.insere(1)
    >>> c2.insere(10)
    >>> c2.em_ordem
    [1, 3, 10, 20]
    >>> c1.intersecao(c2).em_ordem()
    [3, 7]
    >>> c1.remove(12)
    >>> c2.remove(12)
    >>> c1.uniao(c2).em_ordem()
    [1, 3, 7, 10, 20]
    '''

    def __init__(self) -> None:
        '''Cria um novo conjunto vazio'''

    def insere(self, valor: int) -> None:
        '''Insere *valor* no conjunto'''

    def remove(self, valor: int) -> None:
        '''Remove o *valor* do conjunto, se ele estiver presente.'''

    def intersecao(self, outro: Conjunto) -> Conjunto:
        '''Cria um novo conjunto com os elementos que *self* e *outro* têm em comum.'''

    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Cria um novo conjunto com os elementos de *self* e *outro*.'''

    def em_ordem(self) -> list[int]:
        '''Devolve uma lista com os elemento do conjunto em ordem.'''
        
        
