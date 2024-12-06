from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Pessoa:
    '''
    Representa uma pessoa na fila de atendimento.
    '''
    senha: int
    ultrapassado: int    
    
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
SENTINELA_VAZIA = Pessoa(-1, -2)  # Instância de sentinela
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
        nova_pessoa_geral = No(Pessoa(self.senha, 0))
        
        # Em casos gerais, a nova pessoa sempre é inseridade no final.
        self.__auxilia_enfileira(self.sentinela.ante, nova_pessoa_geral)
        
        return self.senha
        
    
    def enfileira_prioridade(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'PRIORIDADE' na fila, garantindo
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
        >>> f.str()
        '[1, 2, 3]'
        '''
        
        sentinela_aux = self.sentinela.ante
        
        # Passando pelos nós até encontrar a posição correta.
        while ((sentinela_aux.item.ultrapassado >= 0) and (sentinela_aux.item.ultrapassado < 2)): 
            sentinela_aux.item.ultrapassado += 1
            sentinela_aux = sentinela_aux.ante
            
        self.senha += 1
        nova_pessoa_prioridade = No(Pessoa(self.senha, -1))
    
        # Após achar a posição correta, a nova pessoa é inserida.
        self.__auxilia_enfileira(sentinela_aux, nova_pessoa_prioridade) 
        return self.senha
    
    
    def desenfileira(self) -> int:
        '''
        Remove um valor no início da fila.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.enfileira_prioridade()
        1
        >>> f.desenfileira()
        1
        >>> f.desenfileira()
        Traceback (most recent call last):
        ...
        ValueError: fila vazia.
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
        >>> f.enfileira_prioridade()
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
        >>> f.enfileira_prioridade()
        2
        >>> f.str()
        '[2, 1]'
        '''
        
        sentinela_aux = self.sentinela.prox
        resultado = '['
        
        if (not self.vazia()):
            resultado += str(sentinela_aux.item.senha)

            sentinela_aux = sentinela_aux.prox
            while (sentinela_aux is not self.sentinela):
                resultado += ", " + str(sentinela_aux.item.senha)
                sentinela_aux = sentinela_aux.prox
        
        return resultado + ']'
    
    
    def __auxilia_enfileira(self, sentinela_aux: No, Novo: No) -> None:
        '''
        Insere uma nova após o nó passado como parametro
            - Após o último nó em casos de senha geral.
            - Após algum nó  geral com ULTRAPASSADO  > 2 ou algum nó de tipo "PRIORIDADE"
        '''
        Novo.ante = sentinela_aux
        Novo.prox = sentinela_aux.prox
        sentinela_aux.prox.ante = Novo
        sentinela_aux.prox = Novo
    