from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    >>> p.desempilha() is None
    True
    '''

    topo: No | None

    def __init__(self) -> None:
        '''
        Cria uma pilha vazia
        '''
        self.topo = None

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        self.topo = No(item, self.topo)

    def desempilha(self) -> str | None:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.
        ou
        Devolve None se a pilha estiver vazia.
        '''
        if self.vazia():
            return None
        
        item = self.topo.item
        self.topo = self.topo.prox
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.
        '''
        return self.topo is None
