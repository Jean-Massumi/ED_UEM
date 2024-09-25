from dataclasses import dataclass

@dataclass
class Data:
    """
    Estrutura que representa uma data composta por dia, mês e ano.

    Atributos:
        dia (int): O dia do mês, deve estar no intervalo de 1 a 31, dependendo do mês.
        mes (int): O mês do ano, deve estar no intervalo de 1 a 12.
        ano (int): O ano, deve ser um número inteiro maior que ou igual a 1.
    """
    dia : int
    mes : int
    ano : int
    
# Exercício 10 - a
def ultimo_dia_ano(data : Data) -> bool:
    """
    Verifica se a *data* fornecida é o último dia do ano.
    
    Parâmetro:
    data (Data):  A data atual representada como uma instância da estrutura Data, que 
    contém os atributos dia, mes e ano.
    
    Retorno:
    bool : Retorna True se a data for o último dia do ano(31 de Dezembro). Caso contrario,
    retorna False.
    
    Exemplos:
    >>> ultimo_dia_ano(Data(31,12,2000))
    True
    >>> ultimo_dia_ano(Data(23,12,1999))
    False
    >>> ultimo_dia_ano(Data(31,10,2020))
    False
    >>> ultimo_dia_ano(Data(11,2,2024))
    False
    """
    
    if data.mes == 12:
        if data.dia == 31:
            return True
    
    return False


# Exercício 10 - b
def data_anterior(d1: Data, d2: Data) -> bool:
    """
    Verifica se a primeira data *d1* vem antes da segunda data *d2*.
    
    Parâmetros:
    d1 : A primeira data a ser comparada, representada como uma instância da estrutura
    Data.
    d2 : A segunda data a ser comparada.
    
    Retorno:
    bool: Retorna True se a primeira data vem antes que a segunda data. Caso contrario, 
    retorna False.
    
    Exemplos:
    >>> data_anterior(Data(12, 1, 2000), Data(12, 1, 2023))
    True
    >>> data_anterior(Data(12, 1, 2000), Data(12, 11, 2000))
    True
    >>> data_anterior(Data(12, 1, 2000), Data(23, 1, 2000))
    True
    >>> data_anterior(Data(12, 1, 2000), Data(12, 1, 2000))
    False
    >>> data_anterior(Data(12, 1, 2000), Data(12, 1, 1988))
    False
    >>> data_anterior(Data(12, 2, 2000), Data(12, 1, 2000))
    False
    >>> data_anterior(Data(12, 1, 2000), Data(9, 1, 2000))
    False
    """
    
    if d1.ano < d2.ano:
        return True
    
    elif d1.ano == d2.ano:
        if d1.mes < d2.mes:
             return True
        
        if d1.mes == d2.mes:
            if d1.dia < d2.dia:
                return True        
        
    return False