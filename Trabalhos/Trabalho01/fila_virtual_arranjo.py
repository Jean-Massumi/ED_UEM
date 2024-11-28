from dataclasses import dataclass
from enum import Enum, auto
from ed import array

# Capacidade inicial alocada para a fila 
CAPACIDADE_INICIAL: int = 5

# Fator de crescimento quando a fila precisa crescer.
FATOR_CRESCIMENTO: int = 2


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
    tipo: Tipo_pessoa | None


# Pessoa que representa uma posição vazia na fila
PESSOA_VAZIA = Pessoa(-1, -1, None)  # Instância de Pessoa

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
    
    fila_valores: array[Pessoa]
    
    tamanho: int
    # Quantidade de pessoas na fila.
    
    senha: int
    # Sequencias de senhas em ordem crescente.
    
    inicio: int
    # Inicio da fila, responsavel por desenfileira.
    
    fim: int
    # Fim da fila, responsavel por enfileira o próximo elemento.
    
    def __init__(self):
        '''
        Inicializa uma nova fila de atendimento.
        
        >>> f = FilaVirtual()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.desenfileira()
        3
        >>> f.desenfileira()
        1
        >>> f.desenfileira()
        2
        >>> f.enfileira_geral()
        4
        >>> f.enfileira_geral()
        5
        >>> f.enfileira_geral()
        6
        >>> f.enfileira_geral()
        7
        >>> f.enfileira_geral()
        8
        >>> f.str()
        '[4, 5, 6, 7, 8]'
        
        '''
        self.fila_valores = array(CAPACIDADE_INICIAL, PESSOA_VAZIA)
        self.senha = 0          # Senha começa em 0.
        self.tamanho = 0
        self.inicio = 0
        self.fim = 0
        
                
        
    def enfileira_geral(self) -> int:
        '''
        Insere a numeração de uma pessoa do tipo 'GERAL' na fila e devolve a 
        numeraçao sequencial atribuído.
                
        Exemplo
        >>> f = FilaVirtual()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        '''
        
        if (self.cheia()):
            self.__cresce()
                
        self.senha += 1
        self.fila_valores[self.fim] = Pessoa(self.senha, 0, Tipo_pessoa.GERAL)
        self.fim = (self.fim + 1) % (len(self.fila_valores))
        self.tamanho += 1
    
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
        
        
        
        # Testando a fila com capacidade inicial
        >>> f = FilaVirtual()
        >>> f.vazia()
        True
        >>> f.cheia()
        False
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.str()
        '[3, 1, 2]'

        # Testando ultrapassagem
        >>> f.enfileira_prioritaria()
        4
        >>> f.enfileira_prioritaria()
        5
        >>> f.str()
        '[3, 4, 1, 2, 5]'

        # Testando desenfileirar
        >>> f.desenfileira()
        3
        >>> f.desenfileira()
        4
        >>> f.str()
        '[1, 2, 5]'

        # Testando crescimento da fila
        >>> for _ in range(10):
        ...     f.enfileira_geral()
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        >>> f.str()  # Deve mostrar todos os elementos na ordem correta
        '[1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]'

        
        '''
    
        if (self.cheia()):
            self.__cresce()
    
        posicao_certa: bool = False   # Acha a posição que deverá ser inserido.
        posicao_atual: int = self.fim - 1    # Contador
        
        while (not posicao_certa):
            pessoa_atual = self.fila_valores[posicao_atual]
            
            if ((pessoa_atual.tipo == Tipo_pessoa.GERAL) and (pessoa_atual.ultrapassado < 2)):
                    
                self.fila_valores[posicao_atual].ultrapassado += 1
                self.fila_valores[posicao_atual + 1] = pessoa_atual
                    
                posicao_atual = (posicao_atual - 1) % (len(self.fila_valores))
                   
            else:                
                posicao_certa = True
                posicao_atual = (posicao_atual + 1) % (len(self.fila_valores))
                
            
        self.senha += 1    
        self.fila_valores[posicao_atual] = Pessoa(self.senha, 0, Tipo_pessoa.PRIORITARIA)
 
        self.tamanho += 1
        self.fim = (self.fim + 1) % (len(self.fila_valores))
    
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
            raise ValueError('Fila vazia')
        
        senha: int = self.fila_valores[self.inicio].senha
        self.inicio = (self.inicio + 1) % (len(self.fila_valores))
        self.tamanho -= 1
    
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
        
        return self.tamanho == 0
    
    
    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia. False caso contrario.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.cheia()
        False
        >>> for i in range(CAPACIDADE_INICIAL):
        ...     f.enfileira_geral()
        1
        2
        3
        4
        5
        >>> f.cheia()
        True
        '''
    
        return self.tamanho == len(self.fila_valores) 
    
    
    
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
        
        resultado = '['
        
        if (not self.vazia()):
            resultado += str(self.fila_valores[self.inicio].senha)
            
            if (self.inicio != 0):
                resultados = self.fim
                
                if (self.fim <= self.inicio):
                    resultados = self.tamanho
                
            else:
                resultados = self.tamanho
            
            for i in range(self.inicio + 1, resultados, 1):
                resultado += ', ' + str(self.fila_valores[i].senha)
            
            if (self.fim <= self.inicio):
                for i in range(0 ,self.fim):
                    resultado += ', ' + str(self.fila_valores[i].senha)
                
        return resultado + ']'
    
    
    def __cresce(self) -> None:
        '''
        Aloca um novo arranjo com a capacidade aumentada por *FATOR_CRESCIMENTO* 
        se *deve_crescer* for verdadeiro.
        
        Aloca um novo arranjo com a mesma capacidade da anterior se *deve_crescer* 
        for Falso.
        
        >>> f = FilaVirtual()
        >>> for i in range(CAPACIDADE_INICIAL * 2):
        ...     f.enfileira_geral()
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        '''    

        capacidade = int(len(self.fila_valores) * FATOR_CRESCIMENTO)
        fila_valores = array(capacidade, PESSOA_VAZIA)

        for i in range(len(self.fila_valores)):
            fila_valores[i] = self.fila_valores[self.inicio]
            self.inicio = (self.inicio + 1) % (len(self.fila_valores))

        self.fila_valores = fila_valores
        
        self.inicio = 0                     # Coloca o indice do início no começo da fila.
        self.fim = self.tamanho             # Coloca o indice a uma posição depois do 
                                            # ultimo elemento da fila anterior.



f = FilaVirtual()
f.vazia()

f.enfileira_geral()
f.enfileira_geral()
f.enfileira_geral()
f.str()

f.enfileira_prioritaria()
f.enfileira_prioritaria()
f.enfileira_prioritaria()
f.str()
