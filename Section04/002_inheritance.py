from abc import abstractmethod,ABC

class Veicle(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self,type,numberOfWheels,fuelType):
        self.veicleType=type
        self.wheelsCount=numberOfWheels
        self.fuelType=fuelType
        
    @abstractmethod
    def engine():
        """_summary_
        """
        pass
    
    @abstractmethod
    def wheels():
        pass
    
    
    @property
    def WHEELS(cls):
        
       return cls.wheelsCount
    


class Car(Veicle):
    
    def __init__(self, type, numberOfWheels, fuelType):
        super().__init__(type, numberOfWheels, fuelType)
        
    def engine(self):
        return "3 Liter Engine"
    
    def wheels(self):
        return "24 inch alloy"
    
        




car1=Car("Car",4,"Petrol")
print(car1.wheels())

print(car1.WHEELS)
    