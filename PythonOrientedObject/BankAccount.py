class Conta:  #class reponsible for project Oriented Object
     #__init__related for construction allocate a data in memory
     #self search value referring in memory
    def __init__(self, numero, titular, saldo, limite):
        print("Objeto alocado na memória {}".format(self))
        self.__numero = numero    #attributes of method         
        self.__titular = titular  #attributes of method  
        self.__saldo = saldo      #attributes of method              
        self.__limite = limite    #attributes of method     

    #extrato rellated with method
    def extrato(self):
        print("O titular é {} com {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        limite_do_saque = self.__saldo + self.__limite
        return  valor_saque <= limite_do_saque

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor      
            print("Saque efeituado com sucesso. Valor em conta de {}" .format(self.__saldo))
        else:
            limite_do_saque = self.__saldo + self.__limite
            print("O valor ultrapassado, saque feito {}, seu limite é de {}" .format(valor, limite_do_saque))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposito(valor)

    @property #get value filled inside attribute
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter #alter value inside of attribute
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod #not need one object to be called, only the class
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
