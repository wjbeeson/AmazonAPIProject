from modules.aplus_module import APlusModule
from modules.aplus_element_validation import ElementValidation
from modules.aplus_element_validation import *
from modules.aplus_element import APlusElement


# noinspection PyTypeChecker
class StandardImageSidebar(APlusModule):
    def __init__(self):
        super().__init__()
        self.name = "Standard Image Sidebar"
        self.headlines = APlusElement(
            name="Headlines",
            validation={
                0: TextElementValidation(max_length=160),
                1: TextElementValidation(max_length=200, required=False),
            }
        )
        self.subheadings = APlusElement(
            name="Subheadings",
            validation={
                0: TextElementValidation(max_length=200)
            }
        )
        self.body_texts = APlusElement(
            name="Body Texts",
            validation={
                0: TextElementValidation(max_length=500),
                1: TextElementValidation(max_length=500, required=False),
            }
        )
        self.bullet_lists = APlusElement(
            name="Bullet Lists",
            validation={
                0: BulletElementValidation(),
                1: BulletElementValidation(),
            }
        )
        self.image_ids = APlusElement(
            name="Image Ids",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=400)),
                1: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=175)),
            }
        )
        self.alt_texts = APlusElement(
            name="Alt Texts",
            validation={
                0: TextElementValidation(max_length=100),
                1: TextElementValidation(max_length=100)
            }
        )
        self.captions = APlusElement(
            name="Captions",
            validation={
                0: TextElementValidation(max_length=100)
            }
        )
