from modules.module import Module
from modules.element_validation import ElementValidation
from modules.element_validation import *
from modules.element import Element


# noinspection PyTypeChecker
class StandardImageSidebar(Module):
    def __init__(self):
        super().__init__()
        self.name = "Standard Image Sidebar"
        self.headlines = Element(
            name="Headlines",
            validation={
                0: TextElementValidation(max_length=160),
                1: TextElementValidation(max_length=200, required=False),
            }
        )
        self.subheadings = Element(
            name="Subheadings",
            validation={
                0: TextElementValidation(max_length=200)
            }
        )
        self.body_texts = Element(
            name="Body Texts",
            validation={
                0: TextElementValidation(max_length=500),
                1: TextElementValidation(max_length=500, required=False),
            }
        )
        self.bullet_lists = Element(
            name="Bullet Lists",
            validation={
                0: BulletElementValidation(),
                1: BulletElementValidation(),
            }
        )
        self.image_ids = Element(
            name="Image Ids",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=400)),
                1: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=175)),
            }
        )
        self.alt_texts = Element(
            name="Alt Texts",
            validation={
                0: TextElementValidation(max_length=100),
                1: TextElementValidation(max_length=100)
            }
        )
        self.captions = Element(
            name="Captions",
            validation={
                0: TextElementValidation(max_length=100)
            }
        )
