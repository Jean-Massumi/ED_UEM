class BancoHoras:
    """
    Um banco de horas que armazena a quantidade de horas e minutos que um funcionário
    trabalhou além da sua jornada normal.
    """
    
    total_horas: int
    total_minutos: int
    
    def __init__(self) -> None:
       """
       Inicializa as variáveis *horas* e *minutos* em 0.
       
       - O banco de horas começa com saldo de 0 horas e 0 minutos.
       
       Exemplos
       >>> bc = BancoHoras()
       >>> bc.consultaSaldo()
       '00:00'
       """ 
       
       self.total_horas = 0
       self.total_minutos = 0
    

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
        
        if (horas >= 0) and (minutos >= 0 and minutos <= 60):
            self.total_horas += horas
            self.total_minutos += minutos
            
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
        >>> bc.saque(0, 40)
        >>> bc.consultaSaldo()
        '00:30'
        """
        
        if ((horas > self.total_horas) or 
                (horas == self.total_horas and minutos > self.total_minutos)):
            raise ValueError(f"Saldo insuficiente! Disponivel: {self.total_horas} horas {self.total_minutos} minutos")
        
        elif (horas < self.total_horas) and (minutos > self.total_minutos):
            self.total_horas -= 1
            self.total_minutos += 60 - minutos
        
        else:
            self.total_horas -= horas
            self.total_minutos -= minutos
    
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
    
        exibir_saldo_str: str
        
        if (self.total_horas >= 10) and ((self.total_minutos >= 10) and (self.total_minutos <= 60)):
            exibir_saldo_str = f"{self.total_horas}:{self.total_minutos}"
        
        elif (self.total_horas < 10) and (self.total_minutos < 10):
            exibir_saldo_str = f"0{self.total_horas}:0{self.total_minutos}"

        elif (self.total_horas < 10):
            exibir_saldo_str = f"0{self.total_horas}:{self.total_minutos}"
    
        elif (self.total_minutos < 10):
            exibir_saldo_str = f"{self.total_horas}:0{self.total_minutos}"
    
        return exibir_saldo_str