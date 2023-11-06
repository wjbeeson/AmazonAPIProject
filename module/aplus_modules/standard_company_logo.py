from module.module import Module
from module.element_validation import *
from module.element import Element
from utility.api_manager import ApiManager


# noinspection PyTypeChecker
class StandardImageLogo(Module):
    def __init__(self):
        super().__init__()
        self.name = "Standard Company Logo"
        self.image_paths = Element(
            name="image_paths",
            validation={
                0: ImageElementValidation(min_resolution=ImageResolution(min_width=600, min_height=180))
            }
        )
        self.alt_texts = Element(
            name="alt_texts",
            validation={
                0: TextElementValidation(max_length=100)
            }
        )

    def _generate_json(self, ):
        image_file = ApiManager().get_image_from_destination_id(self.image_paths.value[0])
        format_dict = {'contentModuleType': 'STANDARD_COMPANY_LOGO', 'standardCompanyLogo': {
            'companyLogo': {'uploadDestinationId': self.image_paths.value[0], 'imageCropSpecification': {
                'size': {'width': {'value': image_file.width, 'units': 'pixels'},
                         'height': {'value': image_file.height, 'units': 'pixels'}},
                'offset': {'x': {'value': 0, 'units': 'pixels'}, 'y': {'value': 0, 'units': 'pixels'}}},
                            'altText': self.alt_texts.value[0]}}, 'standardComparisonTable': None,
                       'standardFourImageText': None, 'standardFourImageTextQuadrant': None,
                       'standardHeaderImageText': None, 'standardImageSidebar': None, 'standardImageTextOverlay': None,
                       'standardMultipleImageText': None, 'standardProductDescription': None,
                       'standardSingleImageHighlights': None, 'standardSingleImageSpecsDetail': None,
                       'standardSingleSideImage': None, 'standardTechSpecs': None, 'standardText': None,
                       'standardThreeImageText': None}
        self.module_dict = format_dict
