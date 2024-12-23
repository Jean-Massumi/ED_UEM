from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None

class Fila:
    '''
    Exemplo para demonstrar que a implementação está incorreta.
    
    >>> f = Fila()
    >>> f.enfileira('oi')
    >>> f.enfileira('tudo')
    >>> f.enfileira('bem?')
    >>> f.desenfileira()
    'oi'
    >>> f.desenfileira()
    'tudo'
    >>> f.desenfileira()
    'bem?'
    >>> f.vazia()
    True
    >>> f.enfileira('abacaxi')
    >>> f.enfileira('beringela')
    >>> f.desenfileira()
    'abacaxi'
    >>> f.desenfileira()
    'beringela'
    '''
    
    inicio: No | None
    fim: No | None
    
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        
        
    def enfileira(self, item: str):
        if self.fim is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox
        
        
    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
                    
        item = self.inicio.item
        self.inicio = self.inicio.prox
        
        if self.inicio is None:  # Condição para que a fila funcione corretamente com
            self.fim = None      # o exemplo que coloquei
        
        return item
    
    
    def vazia(self) -> bool:
        return self.inicio is None
    
    
    
# Resposta: Ao enfileira uma certa quantidade de nó e desenfileira todas elas logo em seguida,
# temos que fazer uma verificação depois que *inicio* receber *inicio.prox* pois se o *inicio*
# é None logo o *fim* terá que ser None. Caso essa verificação não for feita, o fim irá continuar
# enfileirando e o inicio ainda está apontando para o None.