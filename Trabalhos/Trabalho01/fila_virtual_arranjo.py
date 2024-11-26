from dataclasses import dataclass
from enum import Enum, auto
from ed import array

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
    ultrapassado: int
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
    
    fila: array
    
    tamanho: int
    # Quantidade de pessoas na fila.
    
    senha: int
    # Sequencias de senhas em ordem crescente.
    
    capacidade: int
    # Indica o quantidade de elementos de um array.
    
    inicio: int
    
    fim: int
    
    
    def __init__(self, capacidade: int):
        '''
        Inicializa uma nova fila de atendimento.
        '''
        self.fila = array(capacidade + 1, '')
        self.capacidade = capacidade
        self.senha = 0
        self.tamanho = 0
        self.inicio = 0
        self.fim = 0
        
                
        
    def enfileira_geral(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'GERAL' na fila e devolve a 
        numeraçao sequencial atribuído.
                
        Exemplo:
        >>> f = FilaVirtual(20)
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        '''
        
        if (self.cheia):
            raise ValueError('Fila cheia')
        
        self.senha += 1
        self.fila[self.fim] = Pessoa(self.senha, 0, Tipo_pessoa.GERAL)
        self.fim += 1
        self.tamanho += 1
    
        return self.senha
    
    
    def enfileira_prioritaria(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'PRIORITARIA' na fila, garantindo
        que ela tenha precedência sobre as demandas gerais e devolve a numeração
        sequencial atribuído.
        
        Exemplo
        >>> f = FilaVirtual(20)
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
        >>> f = FilaVirtual(20)
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
        >>> f = FilaVirtual(20)
        >>> f.vazia()
        True
        >>> f.enfileira_prioritaria()
        1
        >>> f.vazia()
        False
        '''
        
        return self.tamanho == 0
    
    
    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia. False caso contrario.
        
        Exemplo
        >>> f = FilaVirtual(2)
        >>> f.cheia()
        False
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.cheia()
        True        
        '''
    
        return self.tamanho == self.capacidade 
    
    
    
    def str(self) -> str:
        '''
        Gera uma representação em str da lista.
        
        Exemplo
        >>> f = FilaVirtual(10)
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
    
    
    
        
        
        