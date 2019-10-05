from cuenta import Cuenta

class Black(Cuenta):

    def __init__(self, cbu, balance, fecha_mov):
        super().__init__(cbu, balance, fecha_mov)
    
    def debito(self, monto, banco):
        if banco.lower() == 'banelco':


    def credito(self, monto):
        pass