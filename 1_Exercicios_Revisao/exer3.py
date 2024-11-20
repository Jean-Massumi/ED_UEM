def dma_para_amd(data: str)-> str:
    '''
    Transforma *data*, que deve estar no formato "dia/mes/ano",
    onde dia e mes tem dois dígitos e ano tem quatro dígitos,
    para o formato "ano/mes/dia".
    
    Exemplos:
    >>> dma_para_amd("12/05/2009")
    '2009/05/12'
    >>> dma_para_amd("30/11/1978")
    '1978/11/30'
    >>> dma_para_amd("23/09/2024")
    '2024/09/23'

    '''   
    
    return data[-4:] + "/" +  data[3:5] + "/" + data[0:2]