from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No 
    
    def __init__(self, item: int) -> None:
        self.item = item
        self.prox = None    # type: ignore
    
class Lista:
    '''
    Uma sequência de números.

    Exemplos
    >>> lst = Lista()
    >>> lst.str()
    '[]'
    >>> lst.insere(0, 7)
    >>> lst.insere(1, 20)
    >>> lst.insere(2, 5)
    >>> lst.get(0)
    7
    >>> lst.get(2)
    5
    >>> lst.num_itens()
    3
    >>> lst.str()
    '[7, 20, 5]'
    >>> lst.set(0, 10)
    >>> lst.str()
    '[10, 20, 5]'
    >>> lst.insere(1, 8)
    >>> lst.str()
    '[10, 8, 20, 5]'
    >>> lst.remove(2)
    >>> lst.str()
    '[10, 8, 5]'
    >>> lst.insere(lst.num_itens(), 8)
    >>> lst.str()
    '[10, 8, 5, 8]'
    >>> lst.indice(8)
    1
    >>> lst.remove_item(5)
    >>> lst.str()
    '[10, 8, 8]'
    '''
    
    sentinela: No
    
    tamanho: int
    
    def __init__(self) -> None:
        '''
        Inicializa a sentinela.
        '''

        self.sentinela = No(-1)
        self.sentinela.prox = self.sentinela
        self.tamanho = 0


    def num_itens(self) -> int:
        '''
        Devolve a quantidade de itens da lista.
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.num_itens()
        0
        >>> lst.insere(0, 3)
        >>> lst.num_itens()
        1
        '''
        
        return self.tamanho
    

    def get(self, i: int) -> int:
        '''
        Devolve o item que está na posição *i* da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 3)
        >>> lst.insere(0, 7)
        >>> lst.get(1)
        3
        >>> lst.get(2)
        Traceback (most recent call last):
        ...
        ValueError: índice fora do alcance.
        '''

        if i < 0 or i >= self.num_itens():
            raise ValueError('índice fora do alcance.')    
        
        posicao = 0
        sentinela_aux = self.sentinela.prox
        
        while posicao != i:
            sentinela_aux = sentinela_aux.prox
            posicao += 1
            
        return sentinela_aux.item
    

    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 3)
        >>> lst.insere(0, 7)
        >>> lst.str()
        '[7, 3]'
        >>> lst.set(0, 10)
        >>> lst.str()
        '[10, 3]'
        >>> lst.set(3, 18)
        Traceback (most recent call last):
        ...
        ValueError: índice fora do alcance.
        '''

        if i < 0 or i >= self.num_itens():
            raise ValueError('índice fora do alcance.')    
        
        posicao = 0
        sentinela_aux = self.sentinela.prox
        
        while posicao != i:
            sentinela_aux = sentinela_aux.prox
            posicao += 1
            
        sentinela_aux.item = item    
    

    def insere(self, i: int, item: int):
        '''
        Insere *item* na posição *i* da lista. Os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Requer que 0 <= i <= self.num_itens().
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 2)
        >>> lst.insere(0, 5)
        >>> lst.insere(2, 9)
        >>> lst.insere(1, 1)
        >>> lst.str()
        '[5, 1, 2, 9]'
        >>> lst.insere(5, 11)
        Traceback (most recent call last):
        ...
        ValueError: índice fora do alcance.
        '''

        if i < 0 or i > self.num_itens():
            raise ValueError('índice fora do alcance.')

        novo_no = No(item)
        cont = 0
        sentinela_aux = self.sentinela
        
        while cont != i :
            sentinela_aux = sentinela_aux.prox
            cont += 1
        novo_no.prox = sentinela_aux.prox
        sentinela_aux.prox = novo_no

        self.tamanho += 1


    def remove(self, i: int):
        '''
        Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...

        Requer que 0 <= i < self.num_itens().
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 2)
        >>> lst.insere(0, 5)
        >>> lst.insere(2, 9)
        >>> lst.insere(1, 1)
        >>> lst.remove(2)
        >>> lst.str()
        '[5, 1, 9]'
        >>> lst.remove(0)
        >>> lst.str()
        '[1, 9]'
        >>> lst.remove(1)
        >>> lst.str()
        '[1]'
        >>> lst.remove(0)
        >>> lst.str()
        '[]'
        >>> lst.remove(0)
        Traceback (most recent call last):
        ...
        ValueError: lista vazia
        '''

        if self.vazia():
            raise ValueError('lista vazia')
        
        if i < 0 or i >= self.num_itens():
            raise ValueError('indice fora do alcance.')
        
        sentinela_aux = self.sentinela
        
        for j in range(i):
            sentinela_aux = sentinela_aux.prox
            
        sentinela_aux.prox = sentinela_aux.prox.prox
        self.tamanho -= 1


    def remove_item(self, item: int):
        '''
        Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...

        Requer que *item* esteja na lista.
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 7)
        >>> lst.insere(1, 9)
        >>> lst.insere(1, 11)
        >>> lst.remove_item(11)
        >>> lst.str()
        '[7, 9]'
        '''

        self.remove(self.indice(item))


    def indice(self, item: int) -> int:
        '''
        Devolve a posição da primeira ocorrência de *item* na lista.

        Requer que *item* esteja na lista.
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 2)
        >>> lst.insere(0, 5)
        >>> lst.indice(2)
        1
        >>> lst.indice(7)
        Traceback (most recent call last):
        ...
        ValueError: o item não está na lista.
        '''

        posicao = 0
        sentinela_aux = self.sentinela.prox
        
        while sentinela_aux is not self.sentinela:
            if sentinela_aux.item == item:
                return posicao
            
            sentinela_aux = sentinela_aux.prox
            posicao += 1
    
        raise ValueError('o item não está na lista.')
            

    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.str()
        '[]'
        '''

        representacao = '['
        
        if not self.vazia():
            sentinela_aux = self.sentinela.prox
            
            representacao += str(sentinela_aux.item)
            
            for i in range(1, self.tamanho):
                sentinela_aux = sentinela_aux.prox
                representacao += ', ' + str(sentinela_aux.item)
                
        return representacao + ']'



    def vazia(self) -> bool:
        '''
        Devolve True se a lista está vazia. False caso contrário.
        '''
    
        return self.sentinela.prox is self.sentinela

    
    
    
