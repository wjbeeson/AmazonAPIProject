import module.aplus_modules.standard_image_sidebar
from module import *
from utility import *

import json

def generate_requirements_file():
    possible_modules = {}
    possible_modules['standard_image_sidebar'] = StandardImageSidebar().generate_requirements()
    possible_modules['standard_company_logo'] = StandardImageLogo().generate_requirements()
    with open('module_requirements.json', 'w') as fp:
        json.dump(possible_modules, fp)

def generate_test_input_file():
    user_values_sidebar = ModuleValues(
        headlines=["Headline 1", "Headline 2"],
        subheadings=["Subheading 1"],
        body_texts=["Body Text 1", "Body Text 2"],
        bullet_lists=[["Point 1", "Point 2", "Point 3"], ["Point 1", "Point 2", "Point 3"]],
        image_ids=["C:\\Users\\willb\\Desktop\\pexels-alexander-grey-1212408.jpg",
                   "C:\\Users\\willb\\Desktop\\720b6ff4c1b4ecda848b052cba28c765.jpg"],
        alt_texts=["Alt Text 1", "Alt Text 2"],
        captions=["Caption 1", "Caption 2"]
    )

    user_values_logo = ModuleValues(
        image_ids=[
            "C:\\Users\\willb\\Desktop\\modern-purple-gradient-background-with-sporty-design-cool-gaming-concept-banner-presentation-social-media-certificate-brochure-eps10-vector.jpg"],
        alt_texts=["BOXWAVE Company Logo"]
    )
    user_asin_code = 'B0CJ3FY6S3'
    product_name = "Test Product Name"
    info = {}
    info['asin'] = user_asin_code
    info['product_name'] = product_name
    info['module'] = {}
    info['module'][0] = {}
    info['module'][0]['standard_company_logo'] = user_values_logo.get_dict()
    info['module'][1] = {}
    info['module'][1]['standard_image_sidebar'] = user_values_sidebar.get_dict()
    with open('test_input.json', 'w') as fp:
        json.dump(info, fp)
    pass