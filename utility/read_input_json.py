import json
from module.aplus_modules.standard_company_logo import StandardImageLogo
from module.aplus_modules.standard_image_sidebar import StandardImageSidebar
from module.module import Module
from module.module_values import ModuleValues


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

        # convert input into aplus module
        for i, module_input in enumerate(file_dict['modules'].values()):
            new_module: Module = self.type_dict[list(module_input.keys())[0]]()
            new_module.add_values(ModuleValues.from_dictionary(list(module_input.values())[0]))
            modules.append(new_module)
        return file_dict['asin'], file_dict['product_name'], modules
