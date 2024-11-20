from enum import Enum,auto

class Direcoes(Enum):
    """
    Enumeração que representa as quatro direções cardeais: NORTE, SUL, LESTE e OESTE.
    """
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()
    
    
def direcao_90_graus(direcao : Direcoes) -> Direcoes:
    """
    Devolve a direção de 90 graus no sentido horario, a partir de uma *direcao* fornecida
    
    Parâmetros:
    direcao (Direcoes): Um valor da enumeração que representa as direções(NORTE, SUL, LESTE E OESTE)
    
    Retorno:
    str: A função retorna a direção oposta de uma direção fornecida. 
    Se a entrada for:
    - NORTE, o retorno será LESTE. 
    - SUL, o retorno será OESTE.
    - LESTE, o retorno será SUL.
    - OESTE, o retorno será NORTE.
    
    >>> direcao_90_graus(Direcoes.NORTE).name
    'LESTE'
    >>> direcao_90_graus(Direcoes.SUL).name
    'OESTE'
    >>> direcao_90_graus(Direcoes.LESTE).name
    'SUL'
    >>> direcao_90_graus(Direcoes.OESTE).name
    'NORTE'
    """
    
    if direcao == Direcoes.NORTE:
        angulo_reto = Direcoes.LESTE
        
    elif direcao == Direcoes.SUL:
        angulo_reto = Direcoes.OESTE
        
    elif direcao == Direcoes.LESTE:
        angulo_reto = Direcoes.SUL
    
    elif direcao == Direcoes.OESTE:
        angulo_reto = Direcoes.NORTE
    
    return angulo_reto    