import json

from modules.module import Module
from modules.element_validation import ElementValidation
from modules.element_validation import *
from modules.element import Element
from modules.api_manager import ApiManager


# noinspection PyTypeChecker
class StandardImageSidebar(Module):
    def __init__(self):
        super().__init__()
        self.name = "Standard Image Sidebar"
        self.headlines = Element(
            name="headlines",
            validation={
                0: TextElementValidation(max_length=160)
            }
        )
        self.body_texts = Element(
            name="body_texts",
            validation={
                0: TextElementValidation(max_length=1000)
            }
        )
        self.image_paths = Element(
            name="image_paths",
            # TODO: Hook up image alignment as a definable parameter
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=300), image_position="LEFT")
            }
        )
        self.alt_texts = Element(
            name="alt_texts",
            validation={
                0: TextElementValidation(max_length=100)
            }
        )

    def _generate_json(self):
        manager = ApiManager()
        format_dict = ""
        self.module_dict = format_dict

