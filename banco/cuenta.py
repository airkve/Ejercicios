import datetime

class Cuenta():
    def __init__(self, cbu, balance, fecha_mov):
        self.cbu = cbu
        self.balance = balance
        self.fecha_mov = fecha_mov
        self.fecha = datetime.datetime.now()

    def set_cbu(self, data):
        self.cbu = data

    def set_balance(self, data):
        self.balance = data

    def set_fecha_mov(self, data):
        self.fecha_mov = data
    
    def get_cbu(self):
        pass

    def get_balance(self):
        pass

    def get_fecha_mov(self):
        pass

    def debito(self, monto, banco):
        self.balance -= monto
        print(f'{self.fecha:B% d% Y%}')
        print(f'Estas debitando {monto:.2f} desde {banco}')
        print(f'Tu saldo restante es de: {self.balance:.2f}')