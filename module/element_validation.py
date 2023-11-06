import os.path
import shutil
from abc import ABC, abstractmethod

import PIL.Image
import requests
from PIL import Image


class ElementValidation(ABC):
    def __init__(self):
        self.max_length = None
        self.min_resolution = None
        self.required = None

    @abstractmethod
    def validate_values(self, name, value):
        pass




class ImageResolution():
    def __init__(self, min_width, min_height):
        self.min_width = min_width
        self.min_height = min_height
        self.aspect_fraction = min_width / min_height


class TextElementValidation(ElementValidation):
    def __init__(self, max_length, required=True):
        super().__init__()
        self.max_length = max_length
        self.required = required

    # for images, the value is a text string
    def validate_values(self, name, value):
        if value is None and self.required is False:
            return
        text_string = value
        if text_string is None:
            raise Exception(f"{name} text string must have a value.")
        if len(text_string) > self.max_length:
            raise Exception(f"{name} length must be smaller than {self.max_length} characters")


class BulletElementValidation(ElementValidation):
    def __init__(self, max_length, required=True):
        super().__init__()
        self.max_length = max_length
        self.required = required
    def validate_values(self, name, value: list):
        if value is None and self.required is False:
            return
        bullet_list = value
        if bullet_list.__class__ != list:
            raise Exception ("Bullet Points Must Be in List Format")

        char_count = 0
        for point in bullet_list:
            char_count += len(point)

        if char_count > self.max_length:
            raise Exception(f"{name} length must be smaller than {self.max_length} characters")


class ImageElementValidation(ElementValidation):
    def __init__(self, min_resolution: ImageResolution, image_position=None, required=True):
        super().__init__()
        self.min_resolution = min_resolution
        self.required = required
        self.image_position = image_position

    # for images, the value is an image path
    def validate_values(self, name, value):
        if value is None and self.required is False:
            return
        image_path = value
        if image_path is None:
            raise Exception(f"Image Path must have a value.")
        if not os.path.isfile(image_path):
            response = requests.get(image_path, stream=True)
            if not response.status_code == 200:
                raise Exception(f"Provided Image Path: [{image_path}] is neither a valid filepath or weblink. Please "
                                f"check the location of the source.")
            with open('temp_image.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            image_path = 'temp_image.png'
        try:
            image = PIL.Image.open(image_path)
        except:
            raise Exception(f"Cannot Open Image File: {image_path}")
        wid, hgt = image.size
        if wid < self.min_resolution.min_width or hgt < self.min_resolution.min_height:
            raise Exception(f"Image dimensions for {image_path} are too small. Minimum dimensions are "
                            f"{self.min_resolution.min_width}w by {self.min_resolution.min_height}h")
        if ImageResolution(wid,hgt).aspect_fraction != self.min_resolution.aspect_fraction:
            Exception(f"Image [{image_path}] does not have the same aspect ratio. Please crop and resubmit to be [{self.min_resolution.min_width}w x {self.min_resolution.min_height}h]")
        pass

