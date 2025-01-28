# from __future__ import annotations
# from dataclasses import dataclass

# @dataclass
# class No:
#     val: int
#     prox: No | None
    
# def tira_0(lst: No) -> None:
#     '''
#     Modifica *lst* tirando todas as ocorrências no valor 0.
    
#     Exemplo
    
#     >>> tira_0(None) is None
#     True
#     >>> lst = No(0, No(0, No(23, No(44, None))))
#     >>> lst1 = No(44, No(0, No(0, No(71, None))))
#     >>> lst2 = No(56, No(21, No(0, No(0, None))))
#     >>> lst3 = No(31, No(0, No(0, No(90, No(0, No(56, None))))))
#     >>> tira_0(lst)
#     >>> tira_0(lst1)
#     >>> tira_0(lst2)
#     >>> tira_0(lst3)
#     >>> lst
#     No(val=23, prox=No(val=44, prox=None))
#     >>> lst1
#     No(val=44, prox=No(val=71, prox=None))
#     >>> lst2
#     No(val=56, prox=No(val=21, prox=None))
#     >>> lst3
#     No(val=31, prox=No(val=90, prox=No(val=56, prox=None)))
#     '''

#     if lst is None:
#         return None
    
#     lst = lst.prox
    
    # lst.prox = tira_0(lst.prox)

    # if lst.val == 0:
    #     return lst.prox

    # return lst

# lst = No(0, No(0, No(23, No(44, None))))
# tira_0(lst)
# print(lst)


class No:
    def __init__(self, val=0, prox=None):
        self.val = val
        self.prox = prox
    
    def __str__(self):
        return f"No(val={self.val}, prox={self.prox})"

def tira_0(head):
    # Caso especial: se o nó atual é None, retorna
    if not head:
        return
    
    # Enquanto o próximo existir e for zero, pula ele
    while head.prox and head.prox.val == 0:
        head.prox = head.prox.prox
    
    # Chama recursivamente para o próximo nó
    if head.prox:
        tira_0(head.prox)

# Demonstração
lst1 = No(44, No(0, No(0, No(71, None))))
print("Antes:", lst1)
tira_0(lst1)
print("Depois:", lst1)

# Exemplo com mais casos
lst2 = No(0, No(0, No(1, No(0, No(2, None)))))
print("\nAntes:", lst2)
tira_0(lst2)
print("Depois:", lst2)

