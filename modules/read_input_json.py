import json
import os
from modules.standard_company_logo import StandardImageLogo
from modules.standard_image_sidebar import StandardImageSidebar
from modules.module import Module
from modules.module_values import ModuleValues


class JsonInputReader():
    def __init__(self):
        self.module_dict = {}
        self.type_dict = {}
        self.type_dict['standard_company_logo'] = type(StandardImageLogo())
        self.type_dict['standard_image_sidebar'] = type(StandardImageSidebar())

    def parse_json_into_input(self, json_file):
        # load input json file
        with open(json_file, 'r') as fp:
            file_dict = json.load(fp)
        modules = []

        # convert input into aplus modules
        for i, module in enumerate(file_dict['modules'].values()):
            new_module: Module = self.type_dict[list(module.keys())[0]]()
            new_module.add_values(ModuleValues.from_dictionary(list(module.values())[0]))
            modules.append(new_module)
        return file_dict['asin'], file_dict['product_name'], modules
