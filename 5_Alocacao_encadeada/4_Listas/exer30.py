from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    Um nó no encademaneto.
    '''
    ante: No
    item: int
    prox: No

    def __init__(self, item: int):
        # Após a criação de um nó temos a responsabilidade
        # de alterar ante e prox para valores válidos!
        self.prox = None  # type: ignore
        self.item = item
        self.ante = None  # type: ignore
        
        
def insere(atual: No, novo: No) -> None:
    novo.prox = atual.prox
    novo.ante = atual
    atual.prox.ante = novo
    atual.prox = novo
    
def remove(atual: No) -> int:
    atual.ante.prox = atual.prox
    atual.prox.ante = atual.ante
        
    return atual.item
        
        
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
    invertida: bool

    def __init__(self):
        '''
        Inicializa a lista encadeada.
        '''

        self.sentinela = No(-1)
        self.sentinela.ante = self.sentinela
        self.sentinela.prox = self.sentinela
        self.tamanho = 0
        self.invertida = False # False: navega normalmente (prox), True: navega invertido (ante)


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
        ValueError: índice inválido.
        '''

        if (i < 0) or (i >= self.tamanho):
            raise ValueError('índice inválido.')   
        
        atual = self._prox(self.sentinela)
        for j in range(i):
            atual = self._prox(atual)

        return atual.item
    

    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.insere(0, 3)
        >>> lst.insere(1, 7)
        >>> lst.insere(2, 11)
        >>> lst.str()
        '[3, 7, 11]'
        >>> lst.set(2, 18)
        >>> lst.set(0, 22)
        >>> lst.str()
        '[22, 7, 18]'
        >>> lst.set(3, 18)
        Traceback (most recent call last):
        ...
        ValueError: índice fora do alcance.
        '''

        if i < 0 or i >= self.num_itens():
            raise ValueError('índice fora do alcance.')    
        
        atual = self._prox(self.sentinela)
        for j in range(i):
            atual = self._prox(atual)
  
        atual.item = item
        

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

        novo = No(item)
        atual = self.sentinela
        for j in range((i + 1) if self.invertida else i):
            atual = self._prox(atual)     
            
        insere(atual, novo)
        
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
        
        if i < 0 or i > self.num_itens():
            raise ValueError('índice fora do alcance.')

        atual = self._prox(self.sentinela)
        for j in range(i):
            atual = self._prox(atual)
            
        remove(atual)
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
        atual = self._prox(self.sentinela)
        
        for i in range(self.tamanho):
            if atual.item == item:
                return i
            
            atual = self._prox(atual)

        raise ValueError('o item não está na lista.')


    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        
        Exemplo:
        >>> lst = Lista()
        >>> lst.str()
        '[]'
        '''

        if self.vazia():
            return '[]'
      
        resp = '['
        atual = self._prox(self.sentinela)
        for i in range(self.tamanho - 1):
            resp += str(atual.item) + ', '
            atual = self._prox(atual)
            
        resp += str(atual.item) + ']'
            
        return resp
        
        
    def vazia(self) -> bool:
        '''
        Devolve True se a lista está vazia. False caso contrário.
        '''
    
        return self.sentinela.prox is self.sentinela
    
    
    def inverte(self) -> None:
        '''
        Inverte a direcao da ordem dos elementos da lista.
        
        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(1, 20)
        >>> lst.insere(2, 30)
        >>> lst.str()
        '[10, 20, 30]'
        
        # Testando a inversão básica
        >>> lst.inverte()
        >>> lst.str()
        '[30, 20, 10]'
        
        # Inserção com a lista invertida
        >>> lst.insere(1, 25)
        >>> lst.str()
        '[30, 25, 20, 10]'
        
        # Remoção com a lista invertida
        >>> lst.remove(2)
        >>> lst.str()
        '[30, 25, 10]'
        
        # Verificar com `get` na lista invertida
        >>> lst.get(0)
        30
        >>> lst.get(2)
        10

        # Reinversão para voltar à ordem original
        >>> lst.inverte()
        >>> lst.str()
        '[10, 25, 30]'
        
        # Testando outros métodos na ordem original
        >>> lst.set(1, 27)
        >>> lst.str()
        '[10, 27, 30]'
        >>> lst.remove_item(27)
        >>> lst.str()
        '[10, 30]'
        >>> lst.indice(30)
        1

        # Inverter novamente em uma lista reduzida
        >>> lst.inverte()
        >>> lst.str()
        '[30, 10]'
        '''
        self.invertida = not self.invertida
        
    
    def _prox(self, no: No) -> No:
        '''Retorna o próximo nó considerando o estado de inversão'''
        
        return no.ante if self.invertida else no.prox
    
    