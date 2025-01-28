def tam_max_str(lst: list[str]) -> int:
    '''
    Encontra e devolve a tamanho máximo entre todas as strings de *lst*.
    
    Exemplos
    >>> tam_max_str([])
    0
    >>> tam_max_str(["mouse", "oi", "teto"])
    5
    >>> tam_max_str(["ana", "sertanejo", "lapis"])
    9
    >>> tam_max_str(["navio", "celular", "computadores"])
    12
    '''

    def _tam_max_str(lst: list[str], inicio: int) -> int:
        if inicio == len(lst):
            return 0
        
        else:
            return max(len(lst[inicio]), _tam_max_str(lst, inicio + 1))

    return _tam_max_str(lst, 0)

