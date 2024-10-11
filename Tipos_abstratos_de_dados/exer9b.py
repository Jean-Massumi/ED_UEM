from enum import Enum

class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = 0
    SEG = 1
    TER = 2
    QUA = 3
    QUI = 4
    SEX = 5
    SAB = 6


class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''
    
    dias_selecionados: list

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.dias_selecionados = []    

    def alterna(self, d: Dia):
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''
        
        if str.lower(d.name) in self.dias_selecionados:
            self.dias_selecionados.remove(str.lower(d.name))    
  
        else:
            self.dias_selecionados.append(str.lower(d.name))
            

    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''
        
        dias_da_semana = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]        
        dias_selecionados_ordenado = []

        
        for dia in dias_da_semana:
            if dia in self.dias_selecionados:
                dias_selecionados_ordenado.append(dia)


        return dias_selecionados_ordenado