from __future__ import annotations
from enum import Enum, auto
from ed import array

# Tamanho inicial da tabela hash
TAMANHO_INICIAL = 10

# Fatores para redimensionar a tabela
FATOR_CRESCIMENTO = FATOR_DECRESCIMENTO = 2

# 70% de ocupação máxima para a tabela ser aumentada
FATOR_CARGA_MAXIMA = 0.7

# 20% de ocupação mínima para a tabela ser reduzida
FATOR_CARGA_MINIMA = 0.2

class TipoRemocao(Enum):
    VAZIO = 1       # Posição nunca foi ocupada
    REMOVIDO = 2    # Posição tinha um elemento que foi removido

class Conjunto:
    '''
    Uma coleção de números inteiros distintos.

    Exemplos

    >>> c1 = Conjunto()
    >>> c1.insere(10)
    >>> c1.insere(3)
    >>> c1.insere(12)
    >>> c1.insere(7)
    >>> c1.em_ordem()
    [3, 7, 10, 12]
    >>> c2 = Conjunto()
    >>> c2.insere(20)
    >>> c2.insere(3)
    >>> c2.insere(1)
    >>> c2.insere(10)
    >>> c2.em_ordem()
    [1, 3, 10, 20]
    >>> c1.intersecao(c2).em_ordem()
    [3, 10]
    >>> c1.remove(12)
    >>> c2.remove(12)
    >>> c1.uniao(c2).em_ordem()
    [1, 3, 7, 10, 20]
    '''
    # Array que armazena os elementos do conjunto
    tabela_conjunto: array
    
    # Quantidade atual de elementos no conjunto
    qtd_valores: int

    def __init__(self) -> None:
        '''
        Inicializa um conjunto vazio com tamanho inicial padrão.
        Todas as posições são marcadas inicialmente como VAZIO.
        '''
        
        self.tabela_conjunto = array(TAMANHO_INICIAL, TipoRemocao.VAZIO)
        self.qtd_valores = 0
        

    def insere(self, valor: int) -> None:
        '''
        Insere um valor no conjunto se ele ainda não existir.
        Realiza o redimensionamento da tabela se necessário.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere(20)
        >>> c.insere(10)
        >>> c.insere(5)
        >>> c.insere(30)
        >>> c.insere(40)
        >>> c.insere(25)
        >>> c.insere(8)
        >>> c.insere(2)
        >>> c.insere(6)
        >>> c.insere(9)
        >>> c.insere(12)
        >>> c.insere(14)
        >>> c.em_ordem()
        [2, 5, 6, 8, 9, 10, 12, 14, 20, 25, 30, 40]
        '''

        # Aumenta caso a quantidade seja maior que 70%
        if (self.qtd_valores / len(self.tabela_conjunto)) > FATOR_CARGA_MAXIMA:
            self._cresce()

        # Calcula o índice inicial para inserção
        indice = calcular_indice(valor, len(self.tabela_conjunto))     
        self._auxilia_insere(valor, indice)


    def remove(self, valor: int) -> None:
        '''
        Remove o *valor* do conjunto, se ele estiver presente.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere(20)
        >>> c.insere(10)
        >>> c.insere(5)
        >>> c.insere(30)
        >>> c.insere(40)
        >>> c.insere(25)
        >>> c.insere(8)
        >>> c.insere(2)
        >>> c.insere(6)
        >>> c.insere(9)
        >>> c.insere(12)
        >>> c.insere(14)
        >>> c.remove(9)
        >>> c.remove(2)
        >>> c.remove(12)
        >>> c.remove(14)
        >>> c.em_ordem()
        [5, 6, 8, 10, 20, 25, 30, 40]
        '''
        # Diminui caso a quantidade de elementos seja menor ou igual a 20%
        if (self.qtd_valores / len(self.tabela_conjunto)) <= FATOR_CARGA_MINIMA: 
            self._diminui() 
            
        # Calcula o índice inicial para remoção
        indice = calcular_indice(valor, len(self.tabela_conjunto)) 
        self._auxilia_remocao(valor, indice)


    def intersecao(self, outro: Conjunto) -> Conjunto:
        '''
        Cria um novo conjunto com os elementos que *self* e *outro* têm em comum.
        
        Exemplos
        >>> c1 = Conjunto()
        >>> c1.insere(10)     
        >>> c1.insere(20)      
        >>> c1.insere(5)       
        >>> c1.insere(15)    
        >>> c1.insere(25)      

        # Segundo conjunto
        >>> c2 = Conjunto()
        >>> c2.insere(10)     
        >>> c2.insere(40)     
        >>> c2.insere(30)     
        >>> c2.insere(50)     
        >>> c2.insere(20)     
        
        >>> c1.intersecao(c2).em_ordem()
        [10, 20]
        '''
        conjunto_intersecao = Conjunto()

        def _processar_intersecao(indice: int, tabela_menor: array, tabela_maior: array) -> None:
            if indice == len(tabela_menor):
                return
            
            val = tabela_menor[indice]
            if self._eh_int(val):
                if self._existe_no_conjunto(val, tabela_maior):
                    conjunto_intersecao.insere(val)

            _processar_intersecao(indice + 1, tabela_menor, tabela_maior)      
            
        # Escolhe a menor tabela para iterar (otimização)
        if self.qtd_valores <= outro.qtd_valores:
            _processar_intersecao(0, self.tabela_conjunto, outro.tabela_conjunto)

        else:
            _processar_intersecao(0, outro.tabela_conjunto, self.tabela_conjunto)
        
        return conjunto_intersecao


    def uniao(self, outro: Conjunto) -> Conjunto:
        '''
        Cria um novo conjunto com os elementos de *self* e *outro*.
        
        Exemplos
        >>> c1 = Conjunto()
        >>> c1.insere(10)     
        >>> c1.insere(20)      
        >>> c1.insere(5)       
        >>> c1.insere(15)    
        >>> c1.insere(25)      

        # Segundo conjunto
        >>> c2 = Conjunto()
        >>> c2.insere(10)     
        >>> c2.insere(40)     
        >>> c2.insere(30)     
        >>> c2.insere(50)     
        >>> c2.insere(20)     
        
        >>> c1.uniao(c2).em_ordem()
        [5, 10, 15, 20, 25, 30, 40, 50]
        '''
        conjunto_uniao = Conjunto()
        
        def _faz_uniao(indice: int, tabela: array):
            if indice == len(tabela):
                return
            
            else:
                val = tabela[indice]
                if self._eh_int(val):
                    conjunto_uniao.insere(val)
                    
            _faz_uniao(indice + 1, tabela)
                    
        _faz_uniao(0, self.tabela_conjunto)
        _faz_uniao(0, outro.tabela_conjunto)

        return conjunto_uniao
        
        
    def em_ordem(self) -> list[int]:
        '''
        Devolve uma lista com os elemento do conjunto em ordem.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.em_ordem()
        []
        >>> c.insere(18)
        >>> c.insere(25)
        >>> c.insere(20)
        >>> c.em_ordem()
        [18, 20, 25]
        '''
        
        lista_ordenada = []
        for val in self.tabela_conjunto:
            if  self._eh_int(val):
                lista_ordenada.append(val)
                
        ordena_heap(lista_ordenada)
        
        return lista_ordenada
        
       
    def _existe_no_conjunto(self, val: int, tabela_maior: array) -> bool:
        '''
        Verifica se val está no outro conjunto.
        '''
        indice = calcular_indice(val, len(tabela_maior))
        
        def _localizar_elemento(val: int, t_maior: array, indice: int) -> bool:
            if tabela_maior[indice] == TipoRemocao.VAZIO:
                return False
            
            elif tabela_maior[indice] == val:
                return True

            else: # se val != numero ou val == TipoRemocao.REMOVIDO
                indice = (indice + 1) % len(tabela_maior)
                return _localizar_elemento(val, t_maior, indice)
       
        return _localizar_elemento(val, tabela_maior, indice) 
       
        
    def _auxilia_insere(self, val: int, indice: int) -> None:
        if (self.tabela_conjunto[indice] == TipoRemocao.VAZIO) or \
                (self.tabela_conjunto[indice] == TipoRemocao.REMOVIDO):
            self.tabela_conjunto[indice] = val
            self.qtd_valores += 1
            
        elif self.tabela_conjunto[indice] == val:
            return
            
        else:
            self._auxilia_insere(val, (indice + 1))
            
        
    def _auxilia_remocao(self, val: int, indice: int) -> None:
        if self.tabela_conjunto[indice] == TipoRemocao.VAZIO:
            return

        elif self.tabela_conjunto[indice] == val: #remover e marcar
            self.tabela_conjunto[indice] = TipoRemocao.REMOVIDO  
            self.qtd_valores -= 1

        else: # "/" ou valor numérico
            indice = (indice + 1) % len(self.tabela_conjunto)
            self._auxilia_remocao(val, indice)  
            
            
    def _cresce(self):
        capacidade = int((len(self.tabela_conjunto)) * FATOR_CRESCIMENTO)
        nova_tabela = array(capacidade, TipoRemocao.VAZIO)
        
        tabela_auxiliar = self.tabela_conjunto
        self.tabela_conjunto = nova_tabela

        for val in tabela_auxiliar:
            if  self._eh_int(val):
                indice = calcular_indice(val, capacidade)
                self._auxilia_insere(val, indice)
            
            
    def _diminui(self):
        capacidade = int((len(self.tabela_conjunto)) / FATOR_DECRESCIMENTO)
        nova_tabela = array(capacidade, TipoRemocao.VAZIO)

        tabela_auxiliar = self.tabela_conjunto
        self.tabela_conjunto = nova_tabela

        for val in tabela_auxiliar:
            if self._eh_int(val):
                indice = calcular_indice(val, capacidade)
                self._auxilia_insere(val, indice)


    def _eh_int(self, val: int):
        return val != TipoRemocao.VAZIO and val != TipoRemocao.REMOVIDO

    
       
def inicializa_heap(lst: list[int]) -> None:
    for i in reversed(range(len(lst) // 2)):
        concerta_heap(lst, len(lst), i)
        
        
def ordena_heap(lst: list[int]) -> None:
    inicializa_heap(lst)
    for i in reversed(range(1, len(lst))):

        lst[0], lst[i] = lst[i], lst[0]
        #Concerta a raiz do heap
        concerta_heap(lst, i, 0)
 

                
        
def concerta_heap(lst: list[int], tam: int, i: int):
    assert i < tam <= len(lst)
 
    precisa_ajustar = True
    
    while precisa_ajustar:
        fesq = 2 * i + 1 # 17
        fdir = 2 * i + 2 # 18
        imax = i # 8

        if fesq < tam and lst[fesq] > lst[imax]:
            imax = fesq
            
        if fdir < tam and lst[fdir] > lst[imax]:
            imax = fdir
            
        if imax != i:
            lst[i], lst[imax] = lst[imax], lst[i]
            i = imax
        
        else:
            precisa_ajustar = False
         
        
def calcular_indice(valor: int, tam: int) -> int:
    return valor % tam
