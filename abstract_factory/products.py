from abc import ABC, abstractmethod


class AbstractMac(ABC):
    @abstractmethod
    def mac_so(self):
        pass

    def __str__(self):
        pass

    def install_office_suite(self):
        pass


class AbstractWindows(ABC):
    @abstractmethod
    def win_so(self):
        pass

    def __str__(self):
        pass


class MacBookPro(AbstractMac):
    
    def mac_so(self):
        self._which_so = 'MacOS El Capitan'
        self._name = 'MacBook Pro'
        
    def __str__(self):
        return f'\nThis is a {self._name} that uses {self._which_so}'

    def install_office_suite(self):
        return '\nOffice suite succesfully installed'
    
class MacBookAir(AbstractMac):
    
    def mac_so(self):
        self._which_so = 'MacOS Sierra'
        self._name = 'MacBook Air'
        
    def __str__(self):
        return f'\nThis is a {self._name} that uses {self._which_so}'


class DellComputer(AbstractWindows):

    def win_so(self):
        self._name = 'Dell xps15'
        self._which_so = 'Windows 10'
    
    def __str__(self):
        return f'\nThis is a {self._name} that uses {self._which_so}'


class HPComputer(AbstractWindows):

    def win_so(self):
        self._name = "HP master 23"
        self._which_so = 'Windows 11'
    
    def __str__(self):
        return f'\nThis is a {self._name} that uses {self._which_so}'