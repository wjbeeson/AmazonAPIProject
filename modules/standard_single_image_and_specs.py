
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
                0: TextElementValidation(max_length=200, required=False),
                1: TextElementValidation(max_length=200, required=False),
                2: TextElementValidation(max_length=200, required=False),
            }
        )
        self.subheadings = Element(
            name="subheadings",
            validation={
                0: TextElementValidation(max_length=200, required=False),
                1: TextElementValidation(max_length=160, required=False),
                2: TextElementValidation(max_length=200, required=False),
                3: TextElementValidation(max_length=200, required=False),
            }
        )
        self.body_texts = Element(
            name="body_texts",
            validation={
                0: TextElementValidation(max_length=400),
                1: TextElementValidation(max_length=400),
                2: TextElementValidation(max_length=200, required=False),
            }
        )
        self.bullet_lists = Element(
            name="bullet_lists",
            validation={
                0: BulletElementValidation(max_length=200)
            }
        )
        self.image_paths = Element(
            name="image_paths",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=300)),
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
