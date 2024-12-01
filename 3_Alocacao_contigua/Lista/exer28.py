from ed import array

# Capacidade alocada para a lista
CAPACIDADE = 7

class Lista:
    '''
    Uma sequência de números.

    Exemplos
    # >>> lst = Lista()
    # >>> lst.str()
    # '[]'
    # >>> lst.insere(0, 7)
    # >>> lst.insere(1, 20)
    # >>> lst.insere(2, 5)
    # >>> lst.get(0)
    # 7
    # >>> lst.get(2)
    # 5
    # >>> lst.num_itens()
    # 3
    # >>> lst.str()
    # '[7, 20, 5]'
    # >>> lst.set(0, 10)
    # >>> lst.str()
    # '[10, 20, 5]'
    # >>> lst.insere(1, 8)
    # >>> lst.str()
    # '[10, 8, 20, 5]'
    # >>> lst.remove(2)
    # >>> lst.str()
    # '[10, 8, 5]'
    # >>> lst.insere(lst.num_itens(), 8)
    # >>> lst.str()
    # '[10, 8, 5, 8]'
    # >>> lst.indice(8)
    # 1
    # >>> lst.remove_item(5)
    # >>> lst.str()
    # '[10, 8, 8]'
    '''
    
    valores: array[int]
    
    tamanho: int
    
    inicio: int
    
    def __init__(self):
        '''
        Cria uma nova lista vazia.
        '''
        self.valores = array(CAPACIDADE + 1, 0)
        self.tamanho = 0
        self.inicio = 0
    

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de itens da lista.
        
        Exemplo
        >>> lst = Lista()
        >>> lst.num_itens()
        0
        >>> lst.insere(0, 4)
        >>> lst.insere(0, 7)
        >>> lst.num_itens()
        2
        '''
        
        return self.tamanho
    

    def get(self, i: int) -> int:
        '''
        Devolve o item que está na posição *i* da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo
        >>> lst = Lista()
        >>> lst.insere(0, 8)
        >>> lst.insere(0, 3)        
        >>> lst.get(1)
        8
        >>> lst.get(2)
        Traceback (most recent call last):
        ...
        ValueError: índice 2 fora do alcance!
        '''
        
        if ( (i < 0) or (i >= self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
    
        return self.valores[i]


    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo
        '''
        
        if ( (i < 0) or (i >= self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
        
        self.valores[i] = item
            

    def insere(self, i: int, item: int):
        '''
        Insere *item* na posição *i* da lista. Os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Requer que 0 <= i <= self.num_itens().
        
        Exemplo
        >>> lst = Lista()
        >>> lst.insere(0, 7)
        >>> lst.insere(0, 33)
        >>> lst.insere(0, 80)
        >>> lst.insere(2, 21)
        >>> lst.insere(1, 48)
        >>> lst.str()
        '[80, 48, 33, 21, 7]'
        >>> lst.insere(5, 12)
        Traceback (most recent call last):
        ...
        ValueError: índice 5 fora do alcance!
        '''
       
        if ( (i < 0) or (i > self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
        
        if ((self.tamanho + 1) == len(self.valores)):
            raise ValueError('lista cheia')
        
        metade_tamanho = self.tamanho // 2
        ACHOU_POSICAO = False
        
        if (i <= self.tamanho // 2):
            
            while not ACHOU_POSICAO and metade_tamanho >= 0:
                pre_indice = (self.inicio - (metade_tamanho + 1)) % len(self.valores)
                indice_atual = (self.inicio - metade_tamanho) % len(self.valores)
                
                self.valores[pre_indice] = self.valores[indice_atual]
                
                if (i == metade_tamanho):
                    ACHOU_POSICAO = True
                
                metade_tamanho -= 1
                
            self.inicio = (self.inicio - 1) % len(self.valores)
        
        else:
            tamanho_completo = self.tamanho - 1
            while not ACHOU_POSICAO and tamanho_completo >= metade_tamanho:
                pos_indice = (tamanho_completo + 1) % len(self.valores)
                indice_atual = tamanho_completo % len(self.valores)
                
                self.valores[pos_indice] = self.valores[indice_atual]
                
                if (i == tamanho_completo):
                    ACHOU_POSICAO = True
                
                tamanho_completo -= 1     
        
        self.valores[...] = item
        self.tamanho += 1
        

    def remove(self, i: int):
        '''
        Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...

        Requer que 0 <= i < self.num_itens().
        '''
        raise NotImplemented

    def remove_item(self, item: int):
        '''
        Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...

        Requer que *item* esteja na lista.
        '''
        raise NotImplemented

    def indice(self, item: int) -> int:
        '''
        Devolve a posição da primeira ocorrência de *item* na lista.

        Requer que *item* esteja na lista.
        '''
        raise NotImplemented

    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        '''
        
        resultado = '['
        
        if (self.num_itens() != 0):
            resultado += str(self.valores[self.inicio])
            
            for i in range(1, self.tamanho, 1):
                resultado += ', ' + str(self.valores[(self.inicio + i) % self.tamanho])
                
        return resultado + ']'
        


    def _indice_real(self, i: int) -> int:
        '''
        Converte o índice lógico no índice real no arranjo circular.
        '''
        return (self.inicio + i) % len(self.valores)
