from __future__ import annotations
from arvore_avl import *

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
    
    # Instância da Arvore
    arvore_conjunto: Arvore

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio
        '''
        
        self.arvore_conjunto = None


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
        self.arvore_conjunto = insere_arvore(self.arvore_conjunto , valor)
        

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
        self.arvore_conjunto = remove_arvore(self.arvore_conjunto, valor) 
         


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
        
        novo_conjunto = Conjunto()
        return self._auxilia_intersecao(outro.arvore_conjunto, novo_conjunto)


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

        novo_conjunto = Conjunto()
        return self._auxilia_uniao(outro.arvore_conjunto, novo_conjunto)


    def em_ordem(self) -> list[int]:
        '''
        Devolve uma lista com os elemento do conjunto em ordem.
        '''
        
        lista_conjunto = []   

        return self._auxiliar_em_ordem(self.arvore_conjunto, lista_conjunto)
            

    def _auxilia_intersecao(self, t2: Arvore, novo_conj: Conjunto) -> Conjunto:
        # Função auxiliar para interseção.

        if t2 is not None:
            val = t2.val
            
            if busca(self.arvore_conjunto, val):
                novo_conj.insere(val)
            
            self._auxilia_intersecao(t2.esq, novo_conj)
            self._auxilia_intersecao(t2.dir, novo_conj)
            
        return novo_conj
   
    
    def _auxilia_uniao(self, t2: Arvore, novo_conj: Conjunto) -> Conjunto:
        # Função auxiliar para união que usa percurso em ordem.
        
        def percorre_e_insere(t: Arvore):
            if t is not None:
                percorre_e_insere(t.esq)
                novo_conj.insere(t.val)
                percorre_e_insere(t.dir)
        
        # Percorre as duas árvores em ordem
        percorre_e_insere(self.arvore_conjunto)
        percorre_e_insere(t2)
        
        return novo_conj
        
 
    def _auxiliar_em_ordem(self, t: Arvore, lista_conjunto) -> list[int]:
        # Função auxiliar para ordenar os elementos do conjunto.
       
        if t is not None:
            self._auxiliar_em_ordem(t.esq, lista_conjunto)
            lista_conjunto.append(t.val)
            self._auxiliar_em_ordem(t.dir, lista_conjunto)
            
        return lista_conjunto