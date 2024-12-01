from dataclasses import dataclass
from enum import Enum, auto
from ed import array

# Capacidade inicial da fila 
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
    # Estrutura de dados que armazena as pessoas na fila.
    # É implementada como um array circular para melhor eficiência de memória e tempo.
    
    tamanho: int
    # Quantidade de pessoas na fila.
    
    senha: int
    # Contador incremental que gera as senhas em ordem crescente.    
    
    inicio: int
    # Indice que aponta para o inicio da fila, responsavel por desenfileira.
    
    fim: int
    # Indice que aponta para o fim da fila, responsavel por enfileira o próximo elemento.
    
    def __init__(self):
        '''
        Inicializa uma nova fila circular de atendimento.
        '''
        # Inicialmente, ele é alocado com uma capacidade mínima ajustada (+1 para gestão circular).
        self.fila_valores = array(CAPACIDADE_INICIAL + 1, PESSOA_VAZIA)
        self.senha = 0          # Começa em 0 e aumenta em 1 a cada nova pessoa enfileirada.
        self.tamanho = 0
        self.inicio = 0
        self.fim = 0
        
                
        
    def enfileira_geral(self) -> int:
        '''
        Insere uma pessoa do tipo 'GERAL' na fila e devolva a senha atribuída à 
        pessoa geral.
                
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
        self.fim = self.__avanca_indice(self.fim)
        self.tamanho += 1
    
        return self.senha
    
    
    def enfileira_prioritaria(self) -> int:
        '''
        Insere uma pessoa do tipo 'PRIORITARIA' na fila, garantindo que ela tenha
        precedência sobre as demandas gerais, respeitando as regras de ultrapassagem e
        devolva a senha atribuída à pessoa prioritária.
        
        Exemplo
        >>> f = FilaVirtual()
        >>> f.enfileira_prioritaria()
        1
        >>> f.enfileira_prioritaria()
        2
        >>> f.enfileira_prioritaria()
        3
        '''
    
        if (self.cheia()):
            self.__cresce()
                    
        self.senha += 1   
        posicao = self.__acha_posicao_prioritaria() 
        self.fila_valores[posicao] = Pessoa(self.senha, 0, Tipo_pessoa.PRIORITARIA)
 
        self.tamanho += 1
        self.fim = self.__avanca_indice(self.fim)
    
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
        self.inicio = self.__avanca_indice(self.inicio)
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
    
        return (self.fim + 1) == len(self.fila_valores)
    
    
    
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
            
            for i in range(0, self.tamanho - 1, 1):
                resultado += ', ' + str(self.fila_valores[self.__avanca_indice(self.inicio + i)].senha)
            
        return resultado + ']'
 
 
    def __acha_posicao_prioritaria(self) -> int:
        """
        Encontra a posição correta para inserir uma pessoa prioritária,
        deslocando elementos gerais conforme necessário e devolve o indice onde o 
        elemento prioritária deve ser inserido.
        
        Os elementos que estavam inicialmente na posição i, i+1, ..., passam a ficar
        nas posições i+1, i+2, ... 
        """
    
        posicao_encontrada: bool = False              # Encontra a posição que deverá ser inserido.
        indice: int = self.__recua_indice(self.fim)   # Último indice da fila.
        
        while ((not posicao_encontrada) and (indice >= self.inicio)):
            pessoa = self.fila_valores[indice]
            
            # Verifica se é uma pessoa do tipo *GERAL* que ainda pode ser ultrapassado
            if ((pessoa.tipo == Tipo_pessoa.GERAL) and (pessoa.ultrapassado < 2)):
                self.fila_valores[indice].ultrapassado += 1
                self.fila_valores[self.__avanca_indice(indice)] = pessoa
                indice = self.__recua_indice(indice)
                   
            else:                
                posicao_encontrada = True
            
        return self.__avanca_indice(indice)
 
    
    def __cresce(self) -> None:
        '''
        Duplica a capacidade da fila quando necessário, passando todos os elemetos
        da antiga fila para a nova fila mantendo a ordem dos elementos.
        
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

        capacidade = int((len(self.fila_valores) - 1) * FATOR_CRESCIMENTO)
        fila_valores = array(capacidade + 1, PESSOA_VAZIA)
        
        for i in range(self.tamanho):
            fila_valores[i] = self.fila_valores[(self.inicio + i) % len(self.fila_valores)]
            
        self.fila_valores = fila_valores
        
        self.inicio = 0
        self.fim = self.tamanho
             
             
    def __avanca_indice(self, indice: int) -> int:
        '''
        Avança e devolve o novo indice do elemento da fila circular.
        '''
        
        return (indice + 1) % len(self.fila_valores)
              
             
    def __recua_indice(self, indice: int) -> int:
        '''
        Recua e devolve o novo indice do elemento da fila circular.
        '''
         
        return (indice - 1) % len(self.fila_valores)
               