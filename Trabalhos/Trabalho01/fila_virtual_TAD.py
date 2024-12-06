from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Pessoa:
    '''
    Representa uma pessoa na fila de atendimento.
    '''
    numero: int
    ultrapassado: int = 0

class FilaVirtual:
    '''
    Representa uma fila de atendimento. 

    A fila organiza as pessoas em ordem de chegada, garantindo que as pessoas prioritárias
    tenham preferência sobre as gerais. As regras de ultrapassagem de demandas gerais são respeitadas.
    
    Regras:
    - As demandas prioritárias ficam na frente das gerais
    - Cada demanda geral só pode ser “passada” por até duas prioritárias
    
    Exemplo
    >>> f = FilaVirtual()
    >>> f.vazia()
    True
    >>> f.enfileira_geral()
    1
    >>> f.enfileira_geral()
    2
    >>> f.enfileira_geral()
    3
    >>> f.str()
    '[1, 2, 3]'
    >>> f.enfileira_prioridade()
    4
    >>> f.enfileira_prioridade()
    5
    >>> f.enfileira_prioridade()
    6
    >>> f.str()
    '[4, 5, 1, 2, 3, 6]'
    >>> f.enfileira_geral()
    7
    >>> f.enfileira_geral()
    8
    >>> f.enfileira_prioridade()
    9
    >>> f.str()
    '[4, 5, 1, 2, 3, 6, 9, 7, 8]'
    >>> f.enfileira_geral()
    10
    >>> f.enfileira_prioridade()
    11
    >>> f.str()
    '[4, 5, 1, 2, 3, 6, 9, 11, 7, 8, 10]'
    >>> f.vazia()
    False
    >>> f.desenfileira()
    4
    >>> f.desenfileira()
    5
    >>> f.str()
    '[1, 2, 3, 6, 9, 11, 7, 8, 10]'
    >>> while not f.vazia():
    ...     f.desenfileira()
    1
    2
    3
    6
    9
    11
    7
    8
    10
    >>> f.vazia()
    True
    >>> f.str()
    '[]'
    '''

    
    def __init__(self):
        '''
        Inicializa uma nova fila de atendimento.
        '''
        
        return NotImplementedError
        
        
    def enfileira_geral(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'GERAL' na fila e devolve a 
        numeraçao sequencial atribuído.
                
        Exemplo:
        >>> f = FilaVirtual()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        '''
    
        return NotImplementedError
    
    
    def enfileira_prioridade(self) -> int:
        '''
        Insere a numeração de uma pessoa prioritária na fila, garantindo
        que ela tenha precedência sobre as demandas gerais e devolve a numeração
        sequencial atribuído.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.enfileira_prioridade()
        1
        >>> f.enfileira_prioridade()
        2
        >>> f.enfileira_prioridade()
        3
        '''
    
        return NotImplementedError
    
    
    def desenfileira(self) -> int:
        '''
        Remove um valor no início da fila.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_prioridade()
        2
        >>> f.desenfileira()
        2
        '''
    
        return NotImplementedError
    
    
    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia. False caso contrario.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.vazia()
        True
        >>> f.enfileira_prioridade()
        1
        >>> f.vazia()
        False
        '''
        
        return NotImplementedError
    
    
    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia. False caso contrário.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.cheia()
        False
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.cheia()
        True        
        '''
    
        return NotImplementedError  
    
    
    
    def str(self) -> str:
        '''
        Gera uma representação em str da lista.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.str()
        '[]'
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_prioridade()
        2
        >>> f.str()
        '[1, 2]'
        '''
        
        return NotImplementedError
    
    