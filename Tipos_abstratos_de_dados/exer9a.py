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
    
    dias_marcado: list

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.dias_bool = [False, False, False, False, False, False, False]
        self.dias_marcado = []
    

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
        
        self.dias_bool[d.value] = not(self.dias_bool[d.value])
    
  

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
        self.dias_marcado = []
        
        for i in range(len(self.dias_bool)):
            if self.dias_bool[i]:
                if i == 0:
                    self.dias_marcado.append("dom")

                elif i == 1:
                    self.dias_marcado.append("seg")

                elif i == 2:
                    self.dias_marcado.append("ter")
                    
                elif i == 3:
                    self.dias_marcado.append("qua")
                            
                elif i == 4:
                    self.dias_marcado.append("qui")

                elif i == 5:
                    self.dias_marcado.append("sex")
                    
                elif i == 6:
                    self.dias_marcado.append("sab")
                            
                            
        return self.dias_marcado
