from modules.module_values import ModuleValues
from modules.element import Element
class Module():
    def __init__(self):
        self.headlines = None
        self.subheadings = None
        self.body_texts = None
        self.bullet_lists = None
        self.image_paths = None
        self.alt_texts = None
        self.captions = None
        self.example_empty = None

        self.module_dict = {}

    def print_fields(self):
        fields = self.__dict__
        for key in fields:
            print(f"{key}: {fields[key]}")

    def add_values(self, module_values: ModuleValues):
        if self.headlines is not None:
            self.headlines.value = module_values.headings

        if self.subheadings is not None:
            self.subheadings.value = module_values.subheadings

        if self.body_texts is not None:
            self.body_texts.value = module_values.body_texts

        if self.bullet_lists is not None:
            self.bullet_lists.value = module_values.bullet_lists

        if self.image_paths is not None:
            self.image_paths.value = module_values.image_paths

        if self.alt_texts is not None:
            self.alt_texts.value = module_values.alt_texts

        if self.captions is not None:
            self.captions.value = module_values.captions

        if self.example_empty is not None:
            self.example_empty.value = module_values.example_empty

        self._validate_values()
        self._generate_json()

    def _validate_values(self):
        if self.headlines is not None:
            self.headlines.validate_values()

        if self.subheadings is not None:
            self.subheadings.validate_values()

        if self.body_texts is not None:
            self.body_texts.validate_values()

        if self.bullet_lists is not None:
            self.bullet_lists.validate_values()
            for i, bullet_list in enumerate(self.bullet_lists.value.values()):
                text_list = []
                for j, point in enumerate(bullet_list):
                    text_list.append({'position': j + 1, 'text': {'value': point, 'decoratorSet': []}})
                self.bullet_lists.value[i] = text_list

        if self.image_paths is not None:
            self.image_paths.validate_values()

        if self.alt_texts is not None:
            self.alt_texts.validate_values()

        if self.captions is not None:
            self.captions.validate_values()

        if self.example_empty is not None:
            self.example_empty.validate_values()

    def _generate_json(self):
        pass

    def generate_requirements(self):
        module_requirements = {}
        if self.headlines is not None:
            element_requirements = self.headlines.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.subheadings is not None:
            element_requirements = self.subheadings.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.body_texts is not None:
            element_requirements = self.body_texts.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.bullet_lists is not None:
            element_requirements = self.bullet_lists.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.image_paths is not None:
            element_requirements = self.image_paths.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.alt_texts is not None:
            element_requirements = self.alt_texts.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.captions is not None:
            element_requirements = self.captions.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements

        if self.example_empty is not None:
            element_requirements = self.example_empty.get_requirement_dict()
            module_requirements[element_requirements['element_name']] = element_requirements
        return module_requirements
