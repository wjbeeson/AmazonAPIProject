
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
                0: TextElementValidation(max_length=160),
                1: TextElementValidation(max_length=200, required=False),
            }
        )
        self.subheadings = Element(
            name="subheadings",
            validation={
                0: TextElementValidation(max_length=200)
            }
        )
        self.body_texts = Element(
            name="body_texts",
            validation={
                0: TextElementValidation(max_length=500),
                1: TextElementValidation(max_length=500, required=False),
            }
        )
        self.bullet_lists = Element(
            name="bullet_lists",
            validation={
                0: BulletElementValidation(max_length=200),
                1: BulletElementValidation(max_length=200),
            }
        )
        self.image_paths = Element(
            name="image_paths",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=400)),
                1: ImageElementValidation(min_resolution=ImageResolution(min_width=300, min_height=175)),
            }
        )
        self.alt_texts = Element(
            name="alt_texts",
            validation={
                0: TextElementValidation(max_length=100),
                1: TextElementValidation(max_length=100)
            }
        )
        self.captions = Element(

            name="captions",
            validation={
                0: TextElementValidation(max_length=100)
            }
        )

    def _generate_json(self):
        manager = ApiManager()
        format_dict = {'contentModuleType': 'STANDARD_IMAGE_SIDEBAR', 'standardCompanyLogo': None,
                       'standardComparisonTable': None, 'standardFourImageText': None,
                       'standardFourImageTextQuadrant': None, 'standardHeaderImageText': None,
                       'standardImageSidebar': {'headline': {'value': self.headlines.value[0], 'decoratorSet': []},
                                                'imageCaptionBlock': {'image': {
                                                    'uploadDestinationId': manager.get_image_upload_link(
                                                        self.image_paths.value[0]),
                                                    'imageCropSpecification': {
                                                        'size': {'width': {
                                                            'value': Image.open(self.image_paths.value[0]).width,
                                                            'units': 'pixels'},
                                                                 'height': {'value': Image.open(
                                                                     self.image_paths.value[0]).height,
                                                                            'units': 'pixels'}},
                                                        'offset': {'x': {'value': 0, 'units': 'pixels'},
                                                                   'y': {'value': 0, 'units': 'pixels'}}},
                                                    'altText': self.alt_texts.value[0]},
                                                    'caption': {'value': self.captions.value[0],
                                                                'decoratorSet': []}},
                                                'descriptionTextBlock': {
                                                    'headline': {'value': self.subheadings.value[0],
                                                                 'decoratorSet': []},
                                                    'body': {
                                                        'textList': [
                                                            {'value': self.body_texts.value[0], 'decoratorSet': []}]}},
                                                'descriptionListBlock': {'textList': self.bullet_lists.value[0]},
                                                'sidebarImageTextBlock': {'image': {
                                                    'uploadDestinationId': manager.get_image_upload_link(
                                                        self.image_paths.value[1]),
                                                    'imageCropSpecification': {
                                                        'size': {'width': {
                                                            'value': Image.open(self.image_paths.value[1]).width,
                                                            'units': 'pixels'},
                                                                 'height': {'value': Image.open(
                                                                     self.image_paths.value[1]).height,
                                                                            'units': 'pixels'}},
                                                        'offset': {'x': {'value': 0, 'units': 'pixels'},
                                                                   'y': {'value': 0, 'units': 'pixels'}}},
                                                    'altText': self.alt_texts.value[1]},
                                                    'headline': {'value': self.headlines.value[1],
                                                                 'decoratorSet': []}, 'body': {
                                                        'textList': [
                                                            {'value': self.body_texts.value[1], 'decoratorSet': []}]}},
                                                'sidebarListBlock': {'textList': self.bullet_lists.value[1]}},
                       'standardImageTextOverlay': None, 'standardMultipleImageText': None,
                       'standardProductDescription': None, 'standardSingleImageHighlights': None,
                       'standardSingleImageSpecsDetail': None, 'standardSingleSideImage': None,
                       'standardTechSpecs': None, 'standardText': None, 'standardThreeImageText': None}
        self.module_dict = format_dict
