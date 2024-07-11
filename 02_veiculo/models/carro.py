from .veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self._color = color
    
    def __str__(self):
       return f'Marca: {self._brand.ljust(25)} | Modelo: {self._model.ljust(25)} | Cor: {self._color} '

    def start_car():
        print('Carro ligado.')