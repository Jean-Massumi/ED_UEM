def aumentar_nivel(nivel : int, horas_jogadas : int) -> int:
    """
    Calcula o novo *nível* do jogador baseado nas horas jogadas em uma semana.
    
    - Se o jogador jogou entre 4 a 5 horas, permanece no mesmo nível.
    - Se o jogodor jogou abaixo de 4 horas, perde 1 nivel a cada hora que faltou para alcançar
    as 4 horas.
    - Se o jogador jogou acima de 5 horas, aumenta 1 nível para cada hora jogada além das 
    5 horas jogadas, respeitando o limite de 7 níveis.
    
    - O nível do jogador sempre deve permanecer entre 0 e 25
        
    Parâmetros:
    - nivel (int): Nível atual do jogador, deve estar entre 0 e 25.
    - horas_jogadas (int): Quantidade de horas jogadas na semana, deve ser um número positivo.
    
    Retorno:
    - int : O novo nível do jogador, limitado entre 0 e 25.
    
    Exemplos:
    >>> aumentar_nivel(0, 2)
    0
    >>> aumentar_nivel(0, 7)
    2
    >>> aumentar_nivel(0, 20)
    7
    >>> aumentar_nivel(7, 1)
    4
    >>> aumentar_nivel(7, 6)
    8
    >>> aumentar_nivel(25, 8)
    25
    """
    
    novo_nivel = nivel
    if horas_jogadas > 5: 
        muitas_horas = horas_jogadas - 5
        
        if muitas_horas > 7:
            novo_nivel += 7
        
        else:
            novo_nivel += muitas_horas
            
        if novo_nivel > 25:
            novo_nivel = 25
    
    elif horas_jogadas == 4 or horas_jogadas == 5:
        novo_nivel = nivel
    
    else:
        poucas_horas = 4 - horas_jogadas
        novo_nivel -= poucas_horas
        
        if novo_nivel < 0:
            novo_nivel = 0
            
    return novo_nivel