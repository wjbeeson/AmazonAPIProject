from module.module import Module
from module.element_validation import *
from module.element import Element
from utility.api_manager import ApiManager


# noinspection PyTypeChecker
class StandardImageSidebar(Module):
    def __init__(self):
        super().__init__()
        self.name = "Standard Image Sidebar"
        self.headlines = Element(
            name="headlines",
            validation={
                0: TextElementValidation(max_length=200, required=False),
                1: TextElementValidation(max_length=160, required=False),
                2: TextElementValidation(max_length=160, required=False),
                3: TextElementValidation(max_length=160, required=False),
                4: TextElementValidation(max_length=160, required=False),
            }
        )
        self.body_texts = Element(
            name="body_texts",
            validation={
                0: TextElementValidation(max_length=1000, required=False),
                1: TextElementValidation(max_length=1000, required=False),
                2: TextElementValidation(max_length=1000, required=False),
                3: TextElementValidation(max_length=1000, required=False),
            }
        )

        self.image_paths = Element(
            name="image_paths",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=220, min_height=200)),
                1: ImageElementValidation(min_resolution=ImageResolution(min_width=220, min_height=200)),
                2: ImageElementValidation(min_resolution=ImageResolution(min_width=220, min_height=200)),
                3: ImageElementValidation(min_resolution=ImageResolution(min_width=220, min_height=200)),
            }
        )
        self.alt_texts = Element(
            name="alt_texts",
            validation={
                0: TextElementValidation(max_length=100, required=False),
                1: TextElementValidation(max_length=100, required=False),
                2: TextElementValidation(max_length=100, required=False),
                3: TextElementValidation(max_length=100, required=False),
            }
        )


    def _generate_json(self):
        manager = ApiManager()
        format_dict = ""
        self.module_dict = format_dict
