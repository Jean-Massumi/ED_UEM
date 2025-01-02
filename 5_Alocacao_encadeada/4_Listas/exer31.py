from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    Um nó no encademaneto.
    '''
    ante: No
    item: str
    prox: No

    def __init__(self, item: str):
        # Após a criação de um nó temos a responsabilidade
        # de alterar ante e prox para valores válidos!
        self.prox = None  # type: ignore
        self.item = item
        self.ante = None  # type: ignore
        
        
def insere(atual: No, novo: No) -> None:
    novo.prox = atual.prox
    novo.ante = atual
    atual.prox.ante = novo
    atual.prox = novo
    
def remove(atual: No) -> str:
    atual.ante.prox = atual.prox
    atual.prox.ante = atual.ante
        
    return atual.item


class Conjunto:
    '''
    Representa um conjunto (coleção de elementos únicos) 
    
    Exemplos
    >>> c = Conjunto()
    >>> c.insere('04')
    >>> c.insere('09')
    >>> c.insere('02')
    >>> c.insere('07')
    >>> c.insere('04')
    Traceback (most recent call last):
    ...
    ValueError: o elemento já está no conjunto.
    >>> c.str()
    '[02, 04, 07, 09]'
    >>> c.remove('04')
    '04'
    >>> c.remove('02')
    '02'
    >>> c.remove('09')
    '09'
    >>> c.remove('02')
    >>> c.insere('81')
    >>> c. str()
    '[07, 81]'
    >>> c1 = Conjunto()
    >>> c1.insere('19')
    >>> c1.insere('07')
    >>> c1.insere('15')
    >>> c1.insere('21')
    >>> c1.str()
    '[07, 15, 19, 21]'
    >>> c.uniao(c1)
    "['07', '15', '19', '21', '81']"
    >>> c.intersecao(c1)
    "['07']"
    '''

    sentinela: No


    def __init__(self):
        '''
        Inicializa a sentinela do conjunto.
        '''
        
        self.sentinela = No('')
        self.sentinela.ante = self.sentinela
        self.sentinela.prox = self.sentinela


    def insere(self, elem: str):
        '''
        Insere um elemento no conjunto, se o elemento não estiver nele.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere('3')
        >>> c.insere('3')
        Traceback (most recent call last):
        ...
        ValueError: o elemento já está no conjunto.
        >>> c.str()
        '[3]'
        '''
        
        if self.verificaValores(elem):
            raise ValueError('o elemento já está no conjunto.')

        atual = self.sentinela
        while (atual.prox is not self.sentinela) and (elem > atual.prox.item):
            atual = atual.prox

        novo = No(elem)
        insere(atual, novo)
        
    
    def remove(self, elem: str) -> str | None:
        '''
        Remove o elemento do conjunto. Devolve None se o elemento não estiver lá.
        
        Requer que o conjunto não esteja vazia.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.remove('5')
        Traceback (most recent call last):
        ...
        ValueError: conjunto vazio.
        >>> c.insere('3')
        >>> c.insere('4')
        >>> c.remove('3')
        '3'
        >>> c.remove('7')
        >>> c.str()
        '[4]'
        '''

        if self.sentinela.prox is self.sentinela:
            raise ValueError('conjunto vazio.')

        atual = self.sentinela.prox
        while (atual is not self.sentinela) and (elem >= atual.item):
            if (elem == atual.item):
                return remove(atual)
            atual = atual.prox
            
        return None
    
    
    def verificaValores(self, elem) -> bool:
        '''
        Verifica se um elemento pertence ao conjunto.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere(3)
        >>> c.insere(4)
        >>> c.verificaValores(3)
        True
        >>> c.verificaValores(6)
        False
        '''
        
        atual = self.sentinela.prox
        while atual is not self.sentinela and atual.item < elem:
            atual = atual.prox

        return atual is not self.sentinela and atual.item == elem        
        
    
    def str(self) -> str:
        '''
        Devolve uma representação em string do conjunto.
        
        >>> c = Conjunto()
        >>> c.str()
        '[]'
        >>> c.insere(22)
        >>> c.str()
        '[22]'
        '''
        
        if self.sentinela.prox is self.sentinela:
            return '[]'
        
        resp = '[' + str(self.sentinela.prox.item)
        atual = self.sentinela.prox.prox
        while (atual is not self.sentinela):
            resp += ', ' + str(atual.item)
            atual = atual.prox

        return resp + ']'
    
    
    def uniao(self, conj: Conjunto) -> str:
        '''
        Devolve a união de dois conjuntos na forma de lista.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere(100)
        >>> c.insere(73)
        >>> c.insere(89)
        
        >>> c1 = Conjunto()
        >>> c1.insere(134)
        >>> c1.insere(100)
        >>> c.uniao(c1)
        '[73, 89, 100, 134]'
        '''
        
        dono = self.sentinela.prox
        visi = conj.sentinela.prox
        resp = []
            
        if (dono is not self.sentinela) and (visi is not conj.sentinela):

            while (dono is not self.sentinela) or (visi is not conj.sentinela):
                if dono is self.sentinela:
                    item = visi.item
                    visi = visi.prox
                    
                elif visi is conj.sentinela:
                    item = dono.item
                    dono = dono.prox
                    
                elif visi.item == dono.item:
                    item = dono.item
                    dono = dono.prox
                    visi = visi.prox
                    
                elif dono.item < visi.item:
                    item = dono.item
                    dono = dono.prox
                    
                elif visi.item < dono.item:
                    item = visi.item
                    visi = visi.prox
            
                resp.append(item)

        return str(resp)
       
    
    def intersecao(self, conj: Conjunto) -> str:
        '''
        Devolve a interseção de dois conjuntos na forma de lista. Isto é,
        elementos que se repetem nos dois conjuntos.
        
        Exemplos
        >>> c = Conjunto()
        >>> c.insere(100)
        >>> c.insere(73)
        >>> c.insere(89)
        
        >>> c1 = Conjunto()
        >>> c1.insere(134)
        >>> c1.insere(100)
        >>> c.intersecao(c1)
        '[100]'
        '''

        dono = self.sentinela.prox
        visi = conj.sentinela.prox
        resp = []
        
        if (dono is not self.sentinela) and (visi is not conj.sentinela):

            while (dono is not self.sentinela) and (visi is not conj.sentinela):
                if visi.item == dono.item:
                    resp.append(dono.item)
                    dono = dono.prox
                    visi = visi.prox
            
                elif dono.item < visi.item:
                    dono = dono.prox
                    
                elif visi.item < dono.item:
                    visi = visi.prox

        return str(resp)
            
    