from enum import Enum,auto
from exer9b import direcao_90_graus ,Direcoes
    
def direcao_90_graus_anti(direcao : Direcoes) -> Direcoes:
    """
    Devolve a direção de 90 graus no sentido anti-horario, a partir de uma *direcao* fornecida
    
    Parâmetros:
    direcao (Direcoes): Um valor da enumeração que representa as direções(NORTE, SUL, LESTE E OESTE)
    
    Retorno:
    str: A função retorna a direção oposta de uma direção fornecida. 
    Se a entrada for:
    - NORTE, o retorno será LESTE. 
    - SUL, o retorno será OESTE.
    - LESTE, o retorno será SUL.
    - OESTE, o retorno será NORTE.
    
    >>> direcao_90_graus_anti(Direcoes.NORTE).name
    'OESTE'
    >>> direcao_90_graus_anti(Direcoes.SUL).name
    'LESTE'
    >>> direcao_90_graus_anti(Direcoes.LESTE).name
    'NORTE'
    >>> direcao_90_graus_anti(Direcoes.OESTE).name
    'SUL'
    """
    
    return direcao_90_graus(direcao_90_graus(direcao_90_graus(direcao)))