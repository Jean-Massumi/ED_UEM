from __future__ import annotations
from dataclasses import dataclass
from ed import array

@dataclass
class No:
    '''
    Um nó no encademaneto.
    '''
    ante: int
    item: str
    prox: int
    

class FilaDupla:
    '''
    Uma coleção de strings que segue a política de fila dupla, ou seja, os
    elementos podem ser inseridos e removidos de qualquer extremo (aqui
    chamados de início e fim).

    Exemplos
    >>> f = FilaDupla(7)
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

    valores: array[No]
    inicio: No | None
    fim: No | None
    tamanho: int

    def __init__(self, capacidade: int) -> None:
        '''
        Cria uma nova fila vazia.
        '''
        
        self.capacidade = capacidade
        self.valores = array(capacidade + 1, No(-1, '', -1))
        self.indice_inicio = -1
        self.indice_fim = -1
        self.tamanho = 0

    def insere_inicio(self, item: str):
        '''
        Insere *item* no início da fila.
        '''
        
        if self.cheia():
            raise ValueError('fila cheia.')
        
        novo_indice = self.indice_inicio - 1 if self.indice_inicio > 0 else self.capacidade - 1
        if self.vazia():
            self.indice_inicio = self.indice_fim = 0
            self.valores[0] = No(-1, item, -1)
            
        else:
            self.valores[novo_indice] = No(-1, item, self.indice_inicio)
            self.valores[self.indice_inicio].ante = novo_indice
            self.indice_inicio = novo_indice

        self.tamanho += 1


    def remove_inicio(self) -> str:
        '''
        Remove e devolve o item no início da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        item = self.valores[self.indice_inicio].item
        
        if self.tamanho == 1:
            self.indice_inicio = self.indice_fim = -1
        else:
            prox = self.valores[self.indice_inicio].prox
            self.valores[prox].ante = -1
            self.indice_inicio = prox
            
        self.tamanho -= 1
        
        return item

    def insere_fim(self, item: str):
        '''
        Insere *item* no fim da fila.
        '''
        
        if self.cheia():
            raise ValueError('fila cheia.')
        
        novo_indice = (self.indice_fim + 1) % self.capacidade
        
        if self.vazia():
            self.indice_inicio = self.indice_fim = 0
            self.valores[0] = No(-1, item, -1)
        else:
            self.valores[novo_indice] = No(self.indice_fim, item, -1)
            self.valores[self.indice_fim].prox = novo_indice
            self.indice_fim = novo_indice
            
        self.tamanho += 1
        

    def remove_fim(self) -> str:
        '''
        Remove e devolve o item no fim da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        item = self.valores[self.indice_fim].item
        
        if self.tamanho == 1:
            self.indice_inicio = self.indice_fim = -1
        else:
            ante = self.valores[self.indice_fim].ante
            self.valores[ante].prox = -1
            self.indice_fim = ante
            
        self.tamanho -= 1
        
        return item

    def vazia(self) -> bool:
        '''
        Devolve True e a fila está vazia, False caso contrário.
        '''
        return self.tamanho == 0


    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia, False caso contrário.
        '''

        return self.tamanho == self.capacidade

