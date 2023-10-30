from modules.api_manager import ApiManager

from modules.standard_image_sidebar import StandardImageSidebar
from modules.module_values import ModuleValues
import modules

module = modules.standard_image_sidebar.StandardImageSidebar()
user_values = ModuleValues(
    headlines=["Headline 1", "Headline 2"],
    subheadings=["Subheading 1"],
    body_texts=["Body Text 1", "Body Text 2"],
    bullet_lists=["Bullet List 1", "Bullet List 2"],
    image_ids=["C:\\Users\\willb\\Desktop\\image1.jpg", "C:\\Users\\willb\\Desktop\\example_logo.png"],
    alt_texts=["Alt Text 1", "Alt Text 2"],
    captions=["Caption 1", "Caption 2"],
)
module.add_values(user_values)  # does data validation at this step
pass
user_asin_code = 'B0CJ3FY6S3'
manager = ApiManager()
module.headlines.add_values({0: "Hello", 1: "There"})
pass
# upload_destination_id = manager._upload_image_for_aplus_content(image_path="C:\\Users\\willb\\Desktop\\example_logo.png")
content_doc = manager.get_aplus_content_doc(user_asin_code)
pass
response_draft, response_approval = manager.update_aplus_content_doc(user_asin_code, content_doc)
