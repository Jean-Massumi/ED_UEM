from __future__ import annotations
from ed import array

TAMANHO_INICIAL = 10

FATOR_CRESCIMENTO = FATOR_DECRESCIMENTO = 2

FATOR_CARGA_MAXIMA = 0.7

FATOR_CARGA_MINIMA = 0.2
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
    >>> c2.em_ordem
    [1, 3, 10, 20]
    >>> c1.intersecao(c2).em_ordem()
    [3, 7]
    >>> c1.remove(12)
    >>> c2.remove(12)
    >>> c1.uniao(c2).em_ordem()
    [1, 3, 7, 10, 20]
    '''
    
    tabela_conjunto: array
    qtd_itens: int

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio
        '''
        
        self.tabela_conjunto = array(TAMANHO_INICIAL, None)
        self.qtd_itens = 0
        

    def insere(self, valor: int) -> None:
        '''
        Insere *valor* no conjunto
        
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

        if (self.qtd_itens / len(self.tabela_conjunto)) > FATOR_CARGA_MAXIMA:
            self._cresce()

        indice = calcular_indice(valor, len(self.tabela_conjunto))  
        
        self._auxilia_insere(self, valor, indice)


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
        if (self.qtd_itens / len(self.tabela_conjunto)) <= FATOR_CARGA_MINIMO: 
            self._diminui() #implementar
            
        indice = calcular_indice(valor, len(self.tabela_conjunto))
        
        self._auxilia_remocao(valor, indice)


    def intersecao(self, outro: Conjunto) -> Conjunto:
        '''
        Cria um novo conjunto com os elementos que *self* e *outro* têm em comum.
        
        '''

    def uniao(self, outro: Conjunto) -> Conjunto:
        '''
        Cria um novo conjunto com os elementos de *self* e *outro*.
        
        '''

    def em_ordem(self) -> list[int]:
        '''
        Devolve uma lista com os elemento do conjunto em ordem.
        
        '''
        
        
    def _auxilia_insere(self, val: int, indice: int) -> None:
        if (self.tabela_conjunto[indice] is None) or (self.tabela_conjunto[indice] == "/"):
            self.tabela_conjunto[indice] = val
            self.qtd_itens += 1
            
        elif self.tabela_conjunto[indice] == val:
            return
            
        else:
            self._auxilia_insere(val, (indice + 1))
            
        
    def _auxilia_remocao(self, val:int, indice: int) -> None:
        if self.tabela_conjunto[indice] is None:
            return

        elif self.tabela_conjunto[indice] == val: #remover e marcar
            self.tabela_conjunto[indice] = "/"  

        else: # "/" ou valor numérico
            self._auxilia_remocao(val, (indice + 1))  
            
            
    def _cresce(self):
        capacidade = int((len(self.tabela_conjunto)) * FATOR_CRESCIMENTO)
        nova_tabela = array(capacidade, None)
        
        tabela_auxiliar = self.tabela_conjunto
        self.tabela_conjunto = nova_tabela

        for val in (tabela_auxiliar):
            if val is not None or val != "/":
                indice = calcular_indice(val, capacidade)
                self._auxilia_insere(self, val, indice)
            
            
    def _diminui(self):
        capacidade = int((len(self.tabela_conjunto)) / FATOR_DECRESCIMENTO)
        nova_tabela = array(capacidade, None)

        tabela_auxiliar = self.tabela_conjunto
        self.tabela_conjunto = nova_tabela

        for val in (tabela_auxiliar):
            if val is not None or val != "/":
                indice = calcular_indice(val, capacidade)
                self._auxilia_insere(self, val, indice)



    
       
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
        fesq = 2 * i + 1
        fdir = 2 * i + 2
        imax = i

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


def testa_heap():
    # Teste 1: Lista desordenada simples
    print("=== Teste 1 - Lista desordenada simples ===")
    lista1 = [4, 10, 3, 5, 1]
    print("Original:", lista1)
    
    # Testando criação do heap
    lista1_heap = lista1.copy()
    inicializa_heap(lista1_heap)
    print("Após criar heap:", lista1_heap)
    print("É um min-heap válido?", verifica_min_heap(lista1_heap))
    
    # Testando ordenação
    lista1_ordenada = lista1.copy()
    ordena_heap(lista1_ordenada)
    print("Após ordenar:", lista1_ordenada)
    print("Está ordenada?", esta_ordenada(lista1_ordenada))
    print()

    # Teste 2: Lista já ordenada
    print("=== Teste 2 - Lista já ordenada ===")
    lista2 = [1, 2, 3, 4, 5]
    print("Original:", lista2)
    
    lista2_heap = lista2.copy()
    inicializa_heap(lista2_heap)
    print("Após criar heap:", lista2_heap)
    print("É um min-heap válido?", verifica_min_heap(lista2_heap))
    
    lista2_ordenada = lista2.copy()
    ordena_heap(lista2_ordenada)
    print("Após ordenar:", lista2_ordenada)
    print("Está ordenada?", esta_ordenada(lista2_ordenada))
    print()

    # Teste 3: Lista com elementos repetidos
    print("=== Teste 3 - Lista com elementos repetidos ===")
    lista3 = [3, 3, 1, 2, 2]
    print("Original:", lista3)
    
    lista3_heap = lista3.copy()
    inicializa_heap(lista3_heap)
    print("Após criar heap:", lista3_heap)
    print("É um min-heap válido?", verifica_min_heap(lista3_heap))
    
    lista3_ordenada = lista3.copy()
    ordena_heap(lista3_ordenada)
    print("Após ordenar:", lista3_ordenada)
    print("Está ordenada?", esta_ordenada(lista3_ordenada))
    print()

    # Teste 4: Lista com número par de elementos
    print("=== Teste 4 - Lista com número par de elementos ===")
    lista4 = [6, 5, 4, 3, 2, 1]
    print("Original:", lista4)
    
    lista4_heap = lista4.copy()
    inicializa_heap(lista4_heap)
    print("Após criar heap:", lista4_heap)
    print("É um min-heap válido?", verifica_min_heap(lista4_heap))
    
    lista4_ordenada = lista4.copy()
    ordena_heap(lista4_ordenada)
    print("Após ordenar:", lista4_ordenada)
    print("Está ordenada?", esta_ordenada(lista4_ordenada))

def verifica_min_heap(lst):
    """
    Função auxiliar para verificar se a lista é um min-heap válido
    """
    for i in range(len(lst)):
        fesq = 2 * i + 1
        fdir = 2 * i + 2
        
        if fesq < len(lst) and lst[fesq] < lst[i]:
            return False
        if fdir < len(lst) and lst[fdir] < lst[i]:
            return False
    return True

def esta_ordenada(lst):
    """
    Função auxiliar para verificar se a lista está ordenada
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Executar os testes
testa_heap()