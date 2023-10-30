from abc import ABC, abstractmethod
from modules.element_validation import ElementValidation



class Element(ABC):



    def __init__(self, name: object, validation: ElementValidation):
        self.name = name
        self.value = None
        self.validation = validation

    def validate_values(self):
        for key in self.validation:
            try:
                self.validation[key].validate_values(name=self.name, value=self.value[key])
            except:
                raise Exception(f"Module requires more {self.name} values")


