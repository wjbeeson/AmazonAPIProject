from modules.module_values import ModuleValues
from modules.element import Element
class Module():
    def __init__(self):
        self.headlines = None
        self.subheadings = None
        self.body_texts = None
        self.bullet_lists = None
        self.image_ids = None
        self.alt_texts = None
        self.captions = None
        self.example_empty = None

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

        if self.image_ids is not None:
            self.image_ids.value = module_values.image_ids

        if self.alt_texts is not None:
            self.alt_texts.value = module_values.alt_texts

        if self.captions is not None:
            self.captions.value = module_values.captions

        if self.example_empty is not None:
            self.example_empty.value = module_values.example_empty

        self._validate_values()

    def _validate_values(self):
        if self.headlines is not None:
            self.headlines.validate_values()

        if self.subheadings is not None:
            self.subheadings.validate_values()

        if self.body_texts is not None:
            self.body_texts.validate_values()

        if self.bullet_lists is not None:
            self.bullet_lists.validate_values()

        if self.image_ids is not None:
            self.image_ids.validate_values()

        if self.alt_texts is not None:
            self.alt_texts.validate_values()

        if self.captions is not None:
            self.captions.validate_values()

        if self.example_empty is not None:
            self.example_empty.validate_values()