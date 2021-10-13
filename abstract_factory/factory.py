from abc import ABC, abstractmethod
from products import *


class AbstractFactory(ABC):

    @abstractmethod
    def create_mac(self):
        pass

    @abstractmethod
    def create_win(self):
        pass


class ChinaFactory(AbstractFactory):

    def create_mac(self):
        return MacBookAir()

    def create_win(self):
        return DellComputer()


class CaliforniaFactory(AbstractFactory):
    def create_mac(self):
        return MacBookPro()

    def create_win(self):
        return HPComputer()
    
