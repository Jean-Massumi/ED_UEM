
class BancoHoras:
    """
    Um banco de horas que armazena a quantidade de horas e minutos que um funcionário
    trabalhou além da sua jornada normal.
    """
    
    saldo_total_Minutos: int
    
    def __init__(self) -> None:
       """
       Inicializa as variáveis *horas* e *minutos* em 0.
       
       - O banco de horas começa com saldo de 0 horas e 0 minutos.
       
       Exemplos
       >>> bc = BancoHoras()
       >>> bc.consultaSaldo()
       '00:00'
       """ 
       
       self.saldo_total_Minutos = 0
    

    def deposito(self, horas: int, minutos: int) -> None:
        """
        Deposita as *horas* e *minutos* no banco de horas
        
        Pré-condições:
            - As horas devem ser um número inteiro não negativo.
            - Os minutos deverm ser um número inteiro não negativo e menor que 61.
            
        Pós-condições:
            - As horas e minutos são adicionados ao saldo atual.
            
        Erros:
            - Se os minutos forem maiores que 60, exibe uma mensagem de erro e não 
            realiza o depósito.
        
        Exemplos
        >>> bc = BancoHoras()
        >>> bc.deposito(3, 55)
        >>> bc.consultaSaldo()
        '03:55'
        >>> bc.deposito(4, 65)
        Traceback (most recent call last):
            ...
        ValueError: Erro! Limite de minutos ultrapassados. Mínimo 0 e máximo 60 minutos
        >>> bc.deposito(-3, 55)
        Traceback (most recent call last):
            ...
        ValueError: Erro! Impossível depositar horas negativas!
        """ 
        
        if (horas >= 0) and (minutos >= 0) and (minutos <= 60):
            self.saldo_total_Minutos += (horas * 60) + minutos
        
        elif (horas < 0):
            raise ValueError("Erro! Impossível depositar horas negativas!")
        
        elif (minutos < 0 or minutos > 60):
            raise ValueError("Erro! Limite de minutos ultrapassados. Mínimo 0 e máximo 60 minutos")
        
     
    def saque(self, horas: int, minutos: int) -> None: 
        """
        Saca a quantidade de *horas* e *minutos* do banco de horas
        
        Pré-condições:
            - As horas devem ser um número inteiro não negativo.
            - Os minutos devem ser um número inteiro não negativo e menor que 61.
            - O saldo no banco de horas deve ser suficiente para realizar o saque.
            
        Pós-condições:
            - Se o saldo for suficiente, o valor será subtraído corretamente, inclusive com a conversão de horas em minutos, se necessário.
            - Se os minutos disponíveis forem insuficientes, será feita a conversão de horas para minutos para completar o saque.
            - Se o saldo não for suficiente, o saque não será realizado e o saldo permanece inalterado.
        
        Erros:
            - Se o saldo for insuficiente, exibe uma mensagem de erro e não realiza o saque.
            
        Exemplos
        >>> bc = BancoHoras()
        >>> bc.deposito(3, 55)
        >>> bc.consultaSaldo()
        '03:55'
        >>> bc.saque(4, 0)        
        Traceback (most recent call last):
            ...
        ValueError: Saldo insuficiente! Disponivel: 3 horas 55 minutos
        >>> bc.saque(2, 45)
        >>> bc.consultaSaldo()
        '01:10'
        """
        
        saldo_horas: int = self.saldo_total_Minutos // 60
        saldo_minutos: int = self.saldo_total_Minutos % 60
        
        if ((horas > saldo_horas) or (horas == saldo_horas and minutos > saldo_minutos)):
            raise ValueError(f"Saldo insuficiente! Disponivel: {saldo_horas} horas {saldo_minutos} minutos")
        
        else:
            descontar_horas = (horas * 60) + minutos
            self.saldo_total_Minutos -= descontar_horas   
    
    
    def consultaSaldo(self) -> str:
        """
        Consulta o saldo de horas e minutos no formato "HH:MM".

        Pré-condições:
            - Nenhuma.
        
        Pós-condições:
            - Retorna o saldo atual de horas e minutos no formato de string "HH:MM".
            - A string sempre mostra dois dígitos para minutos, por exemplo, "03:05".
        
        Retorno:
            - String formatada no padrão "HH:MM", representando o saldo de horas e minutos.
        
        Exemplos
        >>> bc = BancoHoras()
        >>> bc.deposito(17, 30)
        >>> bc.consultaSaldo()
        '17:30'
        """
    
        saldo_horas: int = self.saldo_total_Minutos // 60
        saldo_minutos: int = self.saldo_total_Minutos % 60
        exibir_saldo_str: str
        
        if (saldo_horas >= 10) and ((saldo_minutos >= 10) and (saldo_minutos <= 60)):
            exibir_saldo_str = f"{saldo_horas}:{saldo_minutos}"
        
        elif (saldo_horas < 10) and (saldo_minutos < 10):
            exibir_saldo_str = f"0{saldo_horas}:0{saldo_minutos}"

        elif (saldo_horas < 10):
            exibir_saldo_str = f"0{saldo_horas}:{saldo_minutos}"
    
        elif (saldo_minutos < 10):
            exibir_saldo_str = f"{saldo_horas}:0{saldo_minutos}"
    
        return exibir_saldo_str