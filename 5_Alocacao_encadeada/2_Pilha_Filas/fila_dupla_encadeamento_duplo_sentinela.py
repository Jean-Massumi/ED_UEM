from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    Um nó no encademaneto.
    '''
    prox: No
    item: str
    ante: No

    def __init__(self, item: str):
        # Após a criação de um nó temos a responsabilidade
        # de alterar ante e prox para valores válidos!
        self.prox = None  # type: ignore
        self.item = item
        self.ante = None  # type: ignore


def insere(p: No, novo: No):
    '''
    Insere o nó *novo* após o nó *p*.
    '''
    novo.prox = p.prox
    novo.ante = p
    p.prox.ante = novo
    p.prox = novo


def remove(p: No) -> str:
    '''
    Remove o nó *p* do encadeamento e devolve o valor do item armazenado nele.
    '''
    p.ante.prox = p.prox
    p.prox.ante = p.ante
    return p.item


class FilaDupla:
    '''
    Uma coleção de strings que segue a política de fila dupla, ou seja, os
    elementos podem ser inseridos e removidos de qualquer extremo (aqui
    chamados de início e fim).

    Exemplos
    >>> f = FilaDupla()
    >>> f.vazia()
    True
    >>> f.insere_inicio('casa')
    >>> f.insere_inicio('minha')
    >>> f.insere_fim('é')
    >>> f.insere_fim('verde')
    >>> f.insere_fim('legal')
    >>> f.insere_fim('né?')
    >>> f.vazia()
    False
    >>> f.remove_inicio()
    'minha'
    >>> f.remove_inicio()
    'casa'
    >>> f.remove_inicio()
    'é'
    >>> f.remove_inicio()
    'verde'
    >>> f.remove_fim()
    'né?'
    >>> f.remove_fim()
    'legal'
    >>> f.remove_inicio()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    >>> f.remove_fim()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    '''

    sentinela: No

    def __init__(self) -> None:
        self.sentinela = No('')
        self.sentinela.prox = self.sentinela
        self.sentinela.ante = self.sentinela

    def insere_inicio(self, item: str):
        '''
        Insere *item* no início da fila.
        '''
        insere(self.sentinela, No(item))

    def remove_inicio(self) -> str:
        '''
        Remove e devolve o item no início da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        return remove(self.sentinela.prox)

    def insere_fim(self, item: str):
        '''
        Insere *item* no fim da fila.
        '''
        insere(self.sentinela.ante, No(item))

    def remove_fim(self) -> str:
        '''
        Remove e devolve o item no fim da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        return remove(self.sentinela.ante)

    def vazia(self) -> bool:
        '''
        Devolve True e a fila está vazia, False caso contrário.
        '''
        return self.sentinela.prox is self.sentinela
