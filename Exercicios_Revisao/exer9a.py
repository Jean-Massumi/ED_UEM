from enum import Enum,auto

class Direcoes(Enum):
    """
    Enumeração que representa as quatro direções cardeais: NORTE, SUL, LESTE e OESTE.
    """
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()
    
    
def direcao_oposta(direcao : Direcoes) -> Direcoes:
    """
    Devolve a direcao oposta de uma *direcao* informada 

    Parâmetros:
    direcao : Um valor da enumeração que representa as direções(NORTE, SUL, LESTE E OESTE)
 
    Retorno:
    str : A função retorna a direção oposta de uma direção fornecida. Se a entrada for:
    - NORTE, o retorno será SUL.
    - SUL, o retorno será NORTE.
    - LESTE, o retorno será OESTE.
    - OESTE, o retorno será LESTE.

    Exemplos:    
    >>> direcao_oposta(Direcoes.NORTE).name
    'SUL'
    >>> direcao_oposta(Direcoes.SUL).name
    'NORTE'
    >>> direcao_oposta(Direcoes.LESTE).name
    'OESTE'
    >>> direcao_oposta(Direcoes.OESTE).name
    'LESTE'
    """    

    if direcao == Direcoes.NORTE:
        oposta = Direcoes.SUL        

    elif direcao == Direcoes.SUL:
        oposta = Direcoes.NORTE
        
    elif direcao == Direcoes.LESTE:
        oposta = Direcoes.OESTE
        
    else:
        oposta = Direcoes.LESTE
        
    return oposta