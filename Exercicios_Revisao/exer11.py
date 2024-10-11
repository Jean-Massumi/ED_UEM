from enum import Enum, auto
from dataclasses import dataclass

class BandeiraTarifaria(Enum):
    """
    Enumeração que indica o sistema de bandeira tarifária, sinalizando os custos de geração
    de energia com base nas condições de fornecimento.
    
    As bandeiras têm os seguintes acréscimos sobre o valor da tarifa básica por kWh:
    
    - VERDE: Sem acréscimo
    - AMARELA: Acréscimo de R$ 0,01874 por kWh
    - VERMELHA1: Acréscimo de R$ 0,03971 por kWh
    - VERMELHA2: Acréscimo de R$ 0,09492 por kWh
    """
    
    VERDE = auto()
    AMARELA = auto()
    VERMELHA1 = auto()
    VERMELHA2 = auto()
    
@dataclass
class Consumo_Energia:
    """
    Representa o consumo de energia elétrica, a tarifa básica por quilowatt-hora (kWh),
    e a bandeira tarifária vigente que afeta o custo final.
    
    - consumo_kwh: O consumo de energia em quilowatt-hora.
    - tarifa_basica: O custo básico por kWh em reais.
    - bandeira: A bandeira tarifária que sinaliza os custos adicionais da energia.
    """
    
    consumo_kwh: float
    tarifa_basica: float
    bandeira: BandeiraTarifaria 

def custo_final(consumo: Consumo_Energia) -> float:
    """
    Calcula o valor final do *consumo* de energia elétrica com base na tarifa básica 
    e na bandeira tarifária.

    Args:
        consumo (Consumo_Energia): Instância da classe ConsumoEnergia, contendo 
        o consumo de kWh, a tarifa básica e a bandeira tarifária.

    Returns:
        float: O valor final que o consumidor deverá pagar
    
    
    Exemplos:
    >>> custo_final(Consumo_Energia(34.9, 0.60, BandeiraTarifaria.VERDE))
    20.94
    >>> custo_final(Consumo_Energia(34.9, 0.60, BandeiraTarifaria.AMARELA))
    21.59
    >>> custo_final(Consumo_Energia(34.9, 0.60, BandeiraTarifaria.VERMELHA1))
    22.33
    >>> custo_final(Consumo_Energia(34.9, 0.60, BandeiraTarifaria.VERMELHA2))
    24.25
    """

    valor_final = consumo.consumo_kwh
    if consumo.bandeira == BandeiraTarifaria.VERDE:
        valor_final *= consumo.tarifa_basica
    
    elif consumo.bandeira == BandeiraTarifaria.AMARELA:
        valor_final *= (consumo.tarifa_basica + 0.01874)
        
    elif consumo.bandeira == BandeiraTarifaria.VERMELHA1:
        valor_final *= (consumo.tarifa_basica + 0.03971)
        
    elif consumo.bandeira == BandeiraTarifaria.VERMELHA2:
        valor_final *= (consumo.tarifa_basica + 0.09492)

    return round(valor_final, 2)