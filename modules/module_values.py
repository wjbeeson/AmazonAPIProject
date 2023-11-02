class ModuleValues:
    def __init__(
            self,
            headlines: list = None,
            subheadings: list = None,
            body_texts: list = None,
            bullet_lists: list = None,
            image_ids: list = None,
            alt_texts: list = None,
            captions: list = None,
            example_empty: list = None,
    ):
        self.headings = None
        self.subheadings = None
        self.body_texts = None
        self.bullet_lists = None
        self.image_paths = None
        self.alt_texts = None
        self.captions = None
        self.example_empty = None

        if headlines is not None:
            self.headings = {}
            for i, value in enumerate(headlines):
                self.headings[i] = value

        if subheadings is not None:
            self.subheadings = {}
            for i, value in enumerate(subheadings):
                self.subheadings[i] = value

        if body_texts is not None:
            self.body_texts = {}
            for i, value in enumerate(body_texts):
                self.body_texts[i] = value

        if bullet_lists is not None:
            self.bullet_lists = {}
            for i, value in enumerate(bullet_lists):
                self.bullet_lists[i] = value

        if image_ids is not None:
            self.image_paths = {}
            for i, value in enumerate(image_ids):
                self.image_paths[i] = value

        if alt_texts is not None:
            self.alt_texts = {}
            for i, value in enumerate(alt_texts):
                self.alt_texts[i] = value

        if captions is not None:
            self.captions = {}
            for i, value in enumerate(captions):
                self.captions[i] = value

        if example_empty is not None:
            self.example_empty = {}
            for i, value in enumerate(example_empty):
                self.example_empty[i] = value


    def get_dict(self):
        result_dict = {}
        if self.headings is not None:
            result_dict['headings'] = self.headings
        if self.subheadings is not None:
            result_dict['subheadings'] = self.subheadings
        if self.body_texts is not None:
            result_dict['body_texts'] = self.body_texts
        if self.bullet_lists is not None:
            result_dict['bullet_lists'] = self.bullet_lists
        if self.image_paths is not None:
            result_dict['image_paths'] = self.image_paths
        if self.alt_texts is not None:
            result_dict['alt_texts'] = self.alt_texts
        if self.captions is not None:
            result_dict['captions'] = self.captions
        if self.example_empty is not None:
            result_dict['example_empty'] = self.example_empty

        return result_dict