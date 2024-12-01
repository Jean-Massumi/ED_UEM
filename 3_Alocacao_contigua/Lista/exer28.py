from ed import array

# Capacidade alocada para a lista
CAPACIDADE = 11

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
        Cria uma nova lista circular vazia com uma capacidade fixa.
        '''
        self.valores = array(CAPACIDADE, 0)
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
    
        return self.valores[self._indice_real(i)]


    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        
        Exemplo
        '''
        
        if ( (i < 0) or (i >= self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
        
        self.valores[self._indice_real(i)] = item
            

    def insere(self, i: int, item: int):
        '''
        Insere *item* na posição *i*. Move os elementos para o extremo mais próximo.
        
        Se *i* >= tamanho // 2, os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Se *i* < tamanho // 2, os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i-1, i-2, ...

        Requer que 0 <= i <= self.num_itens().
        
        Exemplo
        # Insere no início
        >>> lst = Lista()
        >>> lst.insere(0, 4)
        >>> lst.insere(0, 7)
        >>> lst.insere(0, 2)
        >>> lst.str()
        '[2, 7, 4]'
        
        # Insere no final.
        >>> lst = Lista()
        >>> lst.insere(0, 7)
        >>> lst.insere(1, 33)
        >>> lst.insere(2, 80)
        >>> lst.str()
        '[7, 33, 80]'
        >>> lst.insere(4, 12)
        Traceback (most recent call last):
        ...
        ValueError: índice 4 fora do alcance!
        
        # Insere aleatoriamente.
        >>> lst = Lista()
        >>> lst.insere(0, 7)
        >>> lst.insere(0, 33)
        >>> lst.insere(0, 80)
        >>> lst.insere(0, 21)   # [33, 7, 0, 0, 0, 0, 0, 0, 0, 21, 80] --> [21, 80, 33, 7]
        >>> lst.insere(1, 48)   # [33, 7, 0, 0, 0, 0, 0, 0, 21, 48, 80] --> [21, 48, 80, 33, 7]
        >>> lst.insere(3, 99)   # [99, 33, 7, 0, 0, 0, 0, 0, 21, 48, 80] --> [21, 48, 80, 99, 33, 7]
        >>> lst.insere(6, 63)   # [99, 33, 7, 63, 0, 0, 0, 0, 21, 48, 80] --> [21, 48, 80, 99, 33, 7, 63]
        >>> lst.insere(3, 75)   # [75, 99, 33, 7, 63, 0, 0, 0, 21, 48, 80] --> [21, 48, 80, 75, 99, 33, 7, 63]
        >>> lst.insere(0, 34)   # [75, 99, 33, 7, 63, 0, 0, 34, 21, 48, 80] --> [34, 21, 48, 80, 75, 99, 33, 7, 63]
        >>> lst.insere(3, 101)  # [75, 99, 33, 7, 63, 0, 34, 21, 48, 101, 80] --> [34, 21, 48, 101, 80, 75, 99, 33, 7, 63]
        >>> lst.insere(6, 83)   # [75, 83, 99, 33, 7, 63, 34, 21, 48, 101, 80] --> [34, 21, 48, 101, 80, 75, 83, 99, 33, 7, 63]
        >>> lst.str()       
        '[34, 21, 48, 101, 80, 75, 83, 99, 33, 7, 63]'
        '''
       
        if ( (i < 0) or (i > self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
        
        if ((self.tamanho) == len(self.valores)):
            raise ValueError('lista cheia')
        

        if (i < self.tamanho // 2):
    
            for j in range(0, i):
                pre_indice = self._indice_real(j - 1)
                indice_atual = self._indice_real(j)
                
                self.valores[pre_indice] = self.valores[indice_atual]
                
            self.inicio = (self.inicio - 1) % len(self.valores)

        else:

            for j in range(self.tamanho, i, -1):
                pos_indice = self._indice_real(j)
                indice_atual = self._indice_real(j - 1)
                
                self.valores[pos_indice] = self.valores[indice_atual]

        indice_real = self._indice_real(i)

        self.valores[indice_real] = item
        self.tamanho += 1
        

    def remove(self, i: int):
        '''
        Remove o elemento na posição *i*. Move os elementos restantes para o extremo mais próximo.
        
        Se *i* >= tamanho // 2, Os itens que estavam inicialmente nas 
        posições i, i+1, ..., passam a ficar nas posições i-1, i, ...

         Se *i* < tamanho // 2, Os itens que estavam inicialmente nas 
        posições i, i+1, ..., passam a ficar nas posições i+1, i+2, ...


        Requer que 0 <= i < self.num_itens().
        
        Exemplo
        # Insere no final e Remove no final.
        >>> lst = Lista()
        >>> lst.insere(0, 2)
        >>> lst.insere(1, 5)
        >>> lst.insere(2, 3)
        >>> lst.remove(2)
        >>> lst.str()
        '[2, 5]'
        
        # Insere no final e Remove no inicio.
        >>> lst = Lista()
        >>> lst.insere(0, 2)
        >>> lst.insere(1, 5)
        >>> lst.insere(2, 3)
        >>> lst.remove(0)
        >>> lst.str()
        '[5, 3]'

        '''
        
        if ( (i < 0) or (i > self.num_itens()) ):
            raise ValueError(f'índice {i} fora do alcance!')
        
        if (self.tamanho == 0):
            raise ValueError('lista vazia')
        
        if (i < self.tamanho // 2):
        
            for j in range(0, i):
                pre_indice = self._indice_real(j - 1)
                indice_atual = self._indice_real(j)
                
                self.valores[pre_indice] = self.valores[indice_atual]
                
            self.inicio = (self.inicio + 1) % len(self.valores)

        else:

            for j in range(self.tamanho, i, -1):
                pos_indice = self._indice_real(j)
                indice_atual = self._indice_real(j - 1)
                
                self.valores[pos_indice] = self.valores[indice_atual]


        self.tamanho -= 1
        
        
        
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
                resultado += ', ' + str(self.valores[(self.inicio + i) % len(self.valores)])
                
        return resultado + ']'
        


    def _indice_real(self, i: int) -> int:
        '''
        Converte o índice lógico no índice real no arranjo circular.
        '''
        return (self.inicio + i) % len(self.valores)








