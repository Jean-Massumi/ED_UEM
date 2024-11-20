def calcula_imposto(renda : float) -> float:
    """
    Calcula o imposto devido sobre a *renda* de um cidadão com base nas 
    seguintes faixas de tributação:

    - Para rendas até 1000 dinheiros, aplica-se 5% de imposto.
    - Para rendas entre 1000 e 5000 dinheiros, aplica-se 5% de imposto
    sobre os primeiros 1000 dinheiros e 10% de imposto sobre a parte 
    que exceder 1000 dinheiros.
    - Para rendas acima de 5000 dinheiros, aplica-se 5% de imposto sobre
    os primeiros 1000 dinheiros, 10% sobre os 4000 dinheiros seguintes 
    (de 1000 até 5000) e 20% sobre o valor que exceder 5000 dinheiros.
    
    Requer que a *renda* seja um valor positivo
    
    Parâmetros:
    - renda (float) : A renda total do cidadão em dinheiros.
    
    Retorno:
    - float : O valor total do imposto a ser pago sobre a renda.
    
    Exemplos:
    >>> calcula_imposto(950)
    '47.50'
    >>> calcula_imposto(1350)
    '85.00'
    >>> calcula_imposto(4770)
    '427.00'
    >>> calcula_imposto(8233)
    '1096.60'
    
    """
    
    if renda <= 1000:
        imposto = renda * 0.05
    
    elif renda > 1000 and renda <= 5000:
        imposto = (1000 * 0.05) + (renda - 1000) * 0.1
    
    # renda > 5000
    else:
        imposto = (1000 * 0.05) + (4000 * 0.1) + (renda - 5000) * 0.2
        
    return f"{imposto:.2f}"