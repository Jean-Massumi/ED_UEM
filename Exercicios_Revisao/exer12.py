from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Time:
    """
    Representa o desempenho de um time de futebol em um campeonato.
    
    - nome: O nome do time, usado como critério de desempate alfabético.
    - pontos: O número de pontos do time.
    - vitorias: O número de vitórias do time.
    - saldo_gols: A diferença entre gols marcados e sofridos.
    
    """
    
    nome: str
    pontos: int
    vitorias: int
    saldo_gol: int

class Resultado_Partida(Enum):
    """
    Determina o resultado de um time de futebol em uma partida.
    
    - VITORIA: Indica que o time venceu a partida.
    - EMPATE: Indica que a partida terminou empatada.
    """
    VITORIA = auto()
    EMPATE = auto()

def melhor_desempenho_times(t1: Time, t2: Time) ->str:
    """
    Verifica qual dos dois times tem o melhor desempenho, baseado no número de pontos,
    número de vitórias e saldo de gols (diferença entre gols marcados e sofridos)m
    seguidos nessa ordem.

    Caso os críterios anterios empatem, o desempate é realizado em ordem alfabetica de nomes
    
    Args:
        t1 (Time): Instância da classe Time, contendo nome, pontos, vitorias e saldo de gols.
        t2 (Time): Instância da classe Time, contendo nome, pontos, vitorias e saldo de gols.

    Returns:
        str: Nome do time que o melhor desempenho.
    
    >>> melhor_desempenho_times(Time("Santos", 8, 2, 6), Time("Palmeiras", 4, 2, 3))
    'Santos'
    >>> melhor_desempenho_times(Time("Cruzeiro", 5, 2, 6), Time("Paraná", 5, 3, 3))
    'Paraná'
    >>> melhor_desempenho_times(Time("São Paulo", 3, 4, 10), Time("Internacional", 3, 4, 8))
    'São Paulo'
    >>> melhor_desempenho_times(Time("Bahia", 11, 11, 11), Time("Corinthians", 11, 11, 11))
    'Bahia'
    """
    
    time_melhor_desempenho = t2.nome
    if t1.pontos > t2.pontos:
        time_melhor_desempenho = t1.nome
        
    elif t1.pontos == t2.pontos:
        if t1.vitorias > t2.vitorias:
            time_melhor_desempenho = t1.nome
            
        elif t1.vitorias == t2.vitorias:
            if t1.saldo_gol > t2.saldo_gol:
                time_melhor_desempenho = t1.nome
                
            elif t1.saldo_gol == t2.saldo_gol:
                if t1.nome < t2.nome:
                    time_melhor_desempenho = t1.nome
                    
    return time_melhor_desempenho

def atualiza_desempenho_time(time: Time, resultado: Resultado_Partida) -> str:
    """
    Atualiza o desempenho de um *time* a partir de um resultado de uma *partida*

    Args:
        time (Time): Instancia da classe Time, contendo nome, pontos, vitorias e saldo de gols.
        resultado (Resultado_Partida): Instancia da classe Resultado_Partida, contendo VITORIA
        ou EMPATE.

    Returns:
        str: Desempenho atualizado do time com os novos pontos,
    """
    

    