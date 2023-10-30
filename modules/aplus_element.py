from abc import ABC, abstractmethod
from modules.aplus_module import APlusModule
from modules.aplus_element_validation import ElementValidation
from modules.aplus_element_validation import ImageResolution


class APlusElement(ABC):

    def __init__(self, name: object, validation: ElementValidation):
        self.name = name
        self.values = None
        self.validation = validation


    def add_values(self, values: list):
        self.validation.validate_values(values)


