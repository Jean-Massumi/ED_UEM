from dataclasses import dataclass
from enum import Enum, auto

class Tipo_pessoa(Enum):
    '''
    Representa o tipo de atendimento de uma pessoa.
    '''
    GERAL = auto()
    PRIORITARIA = auto()


@dataclass
class Pessoa:
    '''
    Representa uma pessoa na fila de atendimento.
    '''
    numero: int
    ultrapassado: int = 0
    tipo: Tipo_pessoa


class FilaVirtual:
    '''
    Representa uma fila de atendimento. 

    A fila organiza as pessoas em ordem de chegada, garantindo prioridade para 
    demandas prioritárias. As regras de ultrapassagem de demandas gerais são respeitadas.
    
    Regras:
    - As demandas prioritárias ficam na frente das gerais
    - Cada demanda geral só pode ser “passada” por até duas prioritárias
    
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
    
    
    def enfileira_prioritaria(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'PRIORITARIA' na fila, garantindo
        que ela tenha precedência sobre as demandas gerais e devolve a numeração
        sequencial atribuído.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.enfileira_prioritaria()
        1
        >>> f.enfileira_prioritaria()
        2
        >>> f.enfileira_prioritaria()
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
        >>> f.enfileira_prioritaria()
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
        >>> f.enfileira_prioritaria()
        1
        >>> f.vazia()
        False
        '''
        
        return NotImplementedError
    
    
    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia. False caso contrario.
        
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
        >>> f.enfileira_prioritaria()
        2
        >>> f.str()
        '[1, 2]'
        '''
        
        return NotImplementedError
    