from modules.module import Module


class CustomContentDocument:
    def __init__(self, module_list: list, name):
        content_module_list = []
        for i, module in enumerate(module_list):
            content_module_list.append(module.module_dict)
        self.assembled_dict = {'name': name, 'contentType': 'EBC', 'contentSubType': None, 'locale': 'en-US', 'contentModuleList': content_module_list}




