"""Execution element"""

import json
import RPi.GPIO as GPIO

class ExecutionElement:
    """Execution element"""
    def __init__(self, name):
        GPIO.setmode(GPIO.BCM)
        #GPIO.setmode(GPIO.BOARD)
        self.__Id = 0
        self.__Name = name
        self.__AutomaticValue = 0
        self.__Overriden = 0
        self.__OverridenValue = 0
        self.__Gpio = 0
        self.__OldEffectiveValue = 0

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, value):
        self.__Id = value

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, value:str):
        self.__Name = value

    @property
    def Gpio(self):
        return self.__Gpio

    @Gpio.setter
    def Gpio(self, value):
        self.__Gpio = value
        if value > 0:
            GPIO.setup(value, GPIO.IN)

    @property
    def AutomaticValue(self):
        return self.__AutomaticValue

    @AutomaticValue.setter
    def AutomaticValue(self, value):
        self.__AutomaticValue = value
        self.WriteToGpio()

    @property
    def Overriden(self):
        return self.__Overriden

    @Overriden.setter
    def Overriden(self, value:bool):
        self.__Overriden = value
        self.WriteToGpio()

    @property
    def OverridenValue(self):
        return self.__OverridenValue
    
    @OverridenValue.setter
    def OverridenValue(self, value):
        self.__OverridenValue = value
        self.WriteToGpio()

    @property
    def EffectiveValue(self):
        return self.OverridenValue if self.Overriden else self.AutomaticValue

    def WriteToGpio(self):
        if self.Gpio > 0 and self.EffectiveValue != self.__OldEffectiveValue:
            self.__OldEffectiveValue = self.EffectiveValue
            #This is STUPID
            GPIO.setup(self.Gpio, (GPIO.IN if self.EffectiveValue == 0 else GPIO.OUT))
        
    def __str__(self):
        return json.dumps({
            'Id': self.Id,
            'Name': self.Name,
            'Gpio': self.Gpio,
            'AutomaticValue': self.AutomaticValue,
            'Overriden': self.Overriden,
            'OverridenValue': self.OverridenValue,
            'EffectiveValue': self.EffectiveValue
        })
