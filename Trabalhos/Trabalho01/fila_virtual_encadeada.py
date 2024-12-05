from __future__ import annotations
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
    senha: int
    ultrapassado: int
    tipo: Tipo_pessoa
    
    
@dataclass
class No:
    ante: No
    item: Pessoa
    prox: No
    
    def __init__(self, item: Pessoa) -> None:
        self.ante = None    # type: ignore
        self.item = item
        self.prox = None    # type: ignore


# SENTINELA que representa uma posição vazia na fila
SENTINELA_VAZIA = Pessoa(-1, -1, None)  # Instância de sentinela
class FilaVirtual:
    '''
    Representa uma fila de atendimento. 

    A fila organiza as pessoas em ordem de chegada, garantindo prioridade para 
    demandas prioritárias. As regras de ultrapassagem de demandas gerais são respeitadas.
    
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
    >>> f.enfileira_prioritaria()
    4
    >>> f.enfileira_prioritaria()
    5
    >>> f.enfileira_prioritaria()
    6
    >>> f.str()
    '[4, 5, 1, 2, 3, 6]'
    >>> f.enfileira_geral()
    7
    >>> f.enfileira_geral()
    8
    >>> f.enfileira_prioritaria()
    9
    >>> f.str()
    '[4, 5, 1, 2, 3, 6, 9, 7, 8]'
    >>> f.enfileira_geral()
    10
    >>> f.enfileira_prioritaria()
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

    sentinela: No
    
    senha: int
    # Contador incremental que gera as senhas em ordem crescente.    

    
    def __init__(self):
        '''
        Inicializa uma nova fila encadeada de atendimento.
        '''
        
        self.sentinela = No(SENTINELA_VAZIA)
        self.sentinela.ante = self.sentinela
        self.sentinela.prox = self.sentinela
        self.senha = 0 
                
        
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
        >>> f.str()
        '[1, 2]'
        '''
        
        self.senha += 1
        nova_pessoa_geral = No(Pessoa(self.senha, 0, Tipo_pessoa.GERAL))
        
        self.__auxilia_enfileira(self.sentinela.ante, nova_pessoa_geral)
        
        return self.senha
        
    
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
        
        sentinela_aux = self.sentinela.ante
        
        while ((sentinela_aux.item.tipo == Tipo_pessoa.GERAL) and (sentinela_aux.item.ultrapassado < 2)):
            sentinela_aux.item.ultrapassado += 1
            sentinela_aux = sentinela_aux.ante
            
        self.senha += 1
        nova_pessoa_prioritaria = No(Pessoa(self.senha, 0, Tipo_pessoa.PRIORITARIA))
    
        self.__auxilia_enfileira(sentinela_aux, nova_pessoa_prioritaria)
    
        return self.senha
    
    
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
        
        if (self.vazia()):
            raise ValueError('fila vazia.')
        
        senha = self.sentinela.prox.item.senha

        sentinela_aux = self.sentinela.prox
        sentinela_aux.prox.ante = sentinela_aux.ante
        sentinela_aux.ante.prox = sentinela_aux.prox
    
        return senha
    
    
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
        
        return self.sentinela.prox is self.sentinela
        
    
    
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
        '[2, 1]'
        '''
        
        sentinela_aux = self.sentinela
        resultado = '['
        
        if (sentinela_aux.prox is not self.sentinela):
            resultado += str(sentinela_aux.prox.item.senha)

            sentinela_aux = sentinela_aux.prox.prox
            while (sentinela_aux is not self.sentinela):
                resultado += ", " + str(sentinela_aux.item.senha)
                sentinela_aux = sentinela_aux.prox
        
        return resultado + ']'
    
    
    def __auxilia_enfileira(self, sentinela_aux: No, Novo: No) -> None:
        '''
        
        
        '''
        Novo.ante = sentinela_aux
        Novo.prox = sentinela_aux.prox
        sentinela_aux.prox.ante = Novo
        sentinela_aux.prox = Novo
    
f = FilaVirtual()
f.enfileira_geral()  # GER
f.enfileira_prioritaria()  # PRIORITÁR
f.enfileira_geral()  # GER
f.enfileira_prioritaria()  # PRIORITÁR
f.enfileira_prioritaria()  # PRIORITÁR
f.str()   
