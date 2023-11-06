from modules.generate_requirements_admin_file import *
from modules.read_input_json import JsonInputReader

filename = "C:\\Users\\willb\\Downloads\\Telegram Desktop\\test_input_ B0CMBBC34Y (1).json"

(asin, product_name, module_list) = JsonInputReader().parse_json_into_input(filename)
custom_content_doc = CustomContentDocument(module_list, product_name)
response_draft, response_approval = ApiManager().update_aplus_content_doc(asin, custom_content_doc.assembled_dict)
pass

'''
module_sidebar = modules.standard_image_sidebar.StandardImageSidebar()
user_values_sidebar = ModuleValues(
    headlines=["Headline 1", "Headline 2"],
    subheadings=["Subheading 1"],
    body_texts=["Body Text 1", "Body Text 2"],
    bullet_lists=[["Point 1", "Point 2", "Point 3"], ["Point 1", "Point 2", "Point 3"]],
    image_ids=["C:\\Users\\willb\\Desktop\\pexels-alexander-grey-1212408.jpg", "C:\\Users\\willb\\Desktop\\720b6ff4c1b4ecda848b052cba28c765.jpg"],
    alt_texts=["Alt Text 1", "Alt Text 2"],
    captions=["Caption 1", "Caption 2"]
)
module_logo = modules.standard_company_logo.StandardImageLogo()
user_values_logo = ModuleValues(
    image_ids=["C:\\Users\\willb\\Desktop\\modern-purple-gradient-background-with-sporty-design-cool-gaming-concept-banner-presentation-social-media-certificate-brochure-eps10-vector.jpg"],
    alt_texts=["BOXWAVE Company Logo"]
)
module_sidebar.add_values(user_values_sidebar)  # does data validation at this step
module_logo.add_values(user_values_logo)

custom_content_doc = CustomContentDocument([module_logo, module_sidebar], "Test Product Name")

pass
user_asin_code = 'B0CJ3FY6S3'

content_doc = ApiManager().get_aplus_content_doc(user_asin_code)
response_draft, response_approval = ApiManager().update_aplus_content_doc(user_asin_code, custom_content_doc.assembled_dict)
pass
'''