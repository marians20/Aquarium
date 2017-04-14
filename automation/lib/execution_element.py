"""Execution element"""

import json

class ExecutionElement:
    """Execution element"""
    def __init__(self, name):
        self. Id = 0
        self.Name = name
        self.AutomaticValue = 0
        self.Overriden = 0
        self.OverridenValue = 0

    @property
    def Id(self):
        return self.__id
    @Id.setter
    def Id(self, value):
        self.__id = value

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, value:str):
        self.__Name = value

    @property
    def AutomaticValue(self):
        return self.__AutomaticValue

    @AutomaticValue.setter
    def AutomaticValue(self, value):
        self.__AutomaticValue = value

    @property
    def Overriden(self):
        return self.__Overriden

    @Overriden.setter
    def Overriden(self, value:bool):
        self.__Overriden = value

    @property
    def OverridenValue(self):
        return self.__OverridenValue
    
    @OverridenValue.setter
    def OverridenValue(self, value):
        self.__OverridenValue = value

    @property
    def EffectiveValue(self):
        return self.OverridenValue if self.Overriden else self.AutomaticValue

    def __str__(self):
        return json.dumps({
            'Id': self.Id,
            'Name': self.Name,
            'AutomaticValue': self.AutomaticValue,
            'Overriden': self.Overriden,
            'OverridenValue': self.OverridenValue,
            'EffectiveValue': self.EffectiveValue
        })
