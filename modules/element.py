from abc import ABC, abstractmethod
from modules.element_validation import ElementValidation
from modules.element_validation import ImageResolution


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

    def get_requirement_dict(self):
        if self.validation is not None:
            validation = self.validation
            validation: dict
            element_requirements = {}
            element_requirements['element_name'] = self.name
            element_requirements['occurrences_in_module'] = len(validation)
            element_requirements['validation_type'] = str(validation[0].__class__).split(".")[len(str(validation[0].__class__).split("."))-1].split("'")[0]

            element_requirements['constraints'] = {}
            for i, element_input in enumerate(validation.values()):
                element_input: ElementValidation
                definitions = {}
                definitions['max_length'] = element_input.max_length
                definitions['required'] = element_input.required

                image_validation = element_input.min_resolution
                min_width = None
                min_height = None
                if image_validation is not None:
                    min_width = element_input.min_resolution.min_width
                    min_height = element_input.min_resolution.min_height
                definitions['min_width'] = min_width
                definitions['min_height'] = min_height

                element_requirements['constraints'][i] = definitions
            return element_requirements

