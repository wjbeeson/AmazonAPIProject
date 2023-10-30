class APlusModule():
    def __init__(self):
        self.headlines = None
        self.subheadings = None
        self.body_texts = None
        self.bullet_lists = None
        self.image_ids = None
        self.alt_texts = None
        self.captions = None
        self.example_empty = None

    def print_fields(self):
        fields = self.__dict__
        for key in fields:
            print(f"{key}: {fields[key]}")

    def add_values(self):
        fields = self.__dict__
        for element_name in fields:

            pass
