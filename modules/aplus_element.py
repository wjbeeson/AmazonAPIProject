from abc import ABC, abstractmethod
from modules.aplus_module import APlusModule
from modules.aplus_element_validation import ElementValidation
from modules.aplus_element_validation import ImageResolution


class APlusElement(ABC):

    def __init__(self, name: object, validation: ElementValidation):
        self.name = name
        self.value = None
        self.validation = validation

    def validate_values(self):
        self.validation.validate_values(name=self.name, value=self.value)

