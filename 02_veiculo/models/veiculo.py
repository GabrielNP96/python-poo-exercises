from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model


    @abstractmethod
    def start_car():
        pass