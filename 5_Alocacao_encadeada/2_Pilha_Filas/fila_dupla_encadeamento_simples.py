from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


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

    inicio: No | None
    fim: No | None

    def __init__(self) -> None:
        '''
        Cria uma nova fila vazia.
        '''
        
        self.inicio = None
        self.fim = None

    def insere_inicio(self, item: str):
        '''
        Insere *item* no início da fila.
        '''
        
        if self.inicio is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
            
        else:
            self.inicio = No(item, self.inicio)

    def remove_inicio(self) -> str:
        '''
        Remove e devolve o item no início da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is None:
            raise ValueError('fila vazia')
        
        item = self.inicio.item
        self.inicio = self.inicio.prox
        
        if self.inicio is None:
            self.fim = None
            
        return item

    def insere_fim(self, item: str):
        '''
        Insere *item* no fim da fila.
        '''
        
        if self.fim is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
            
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def remove_fim(self) -> str:
        '''
        Remove e devolve o item no fim da fila.

        Requer que a fila não esteja vazia.
        '''
        
        if self.fim is None:
            raise ValueError('fila vazia')

        # Salva o último elemento
        item = self.fim.item

        p = self.inicio
        assert p is not None
        
        # Único elemento?
        if p.prox is None:
            self.inicio = None
            self.fim = None
            
        else:
            # Encontra o penúltimo
            while p.prox is not self.fim:
                p = p.prox
                
            p.prox = None
            self.fim = p

        # Devolve o item
        return item

    def vazia(self) -> bool:
        '''
        Devolve True e a fila está vazia, False caso contrário.
        '''
        return self.inicio is None
