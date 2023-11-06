import json
import os
from pathlib import Path

import requests
import sp_api.base
import shutil

import requests
from dotenv import load_dotenv


class ImageUploader:
    def __init__(self):
        # Setup Environment
        dotenv_path = Path('env/.env')
        load_dotenv(dotenv_path=dotenv_path)

        self.default_marketplace_id = os.environ['MARKETPLACE_ID']
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.refresh_token = os.getenv('REFRESH_TOKEN')
        self.aws_access_key = os.getenv('AWS_ACCESS_KEY')
        self.aws_secret_key = os.getenv('AWS_SECRET_KEY')
        self.aws_region = 'us-east-1'
        self.service = 'execute-api'
        self.temp_image_path = "temp_image.png"

    def _generate_access_token(self):
        token_url = 'https://api.amazon.com/auth/o2/token'
        token_data = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
        }
        token_r = requests.post(token_url, data=token_data)
        token = json.loads(token_r.text)['access_token']
        return token

    def _create_upload_destination(self, image_path):
        # Step 1: Request Access Token
        token = self._generate_access_token()

        # Step 2: Prepare the Request for A+ Content
        method = 'POST'
        host = 'sellingpartnerapi-na.amazon.com'
        uri = '/uploads/2020-11-01/uploadDestinations/aplus/2020-11-01/contentDocuments'
        pass

        with open(image_path, 'rb') as fp:
            md5hash = sp_api.base.helpers.create_md5(fp)

        # Update parameters as needed for the specific A+ Content request
        params = {
            'marketplaceIds': self.default_marketplace_id,
            'contentMD5': md5hash,
            'resource': "aplus/2020-11-01/contentDocuments",
            'contentType': "image/png"
        }

        endpoint = f'https://{host}{uri}'
        headers = {
            'host': host,
            'x-amz-access-token': token,
            'Content-Type': 'application/json'
        }

        # Step 3: Make the API Call
        response = requests.request(
            method=method,
            url=endpoint,
            params=params,
            headers=headers
        )
        payload = response.json()['payload']
        return payload['uploadDestinationId'], payload['url']

    def get_image_upload_destination_id(self, image_path, is_web_request=False):
        if is_web_request:
            response = requests.get(image_path, stream=True)
            with open(self.temp_image_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            image_path = self.temp_image_path
            del out_file
            del response
        # Step 1: create upload destination for aplus image
        upload_destination_id, upload_url = self._create_upload_destination(image_path)

        # Step 2: format parameters for image posting
        params = []
        endpoint = ""
        for element in upload_url.split("&"):
            split = element.split("?")
            if len(split) > 1:
                params.append(split[1])
                endpoint = split[0].rstrip("/")
            else:
                params.append(element)
        data = {}
        for param in params:
            split = param.split("=")
            data[split[0]] = (None, split[1])
            pass

        data['file'] = open(image_path, 'rb')

        # Step 3: Make the Request
        response = requests.post(
            url=endpoint,
            files=data,
        )

        # Step 4: Handle the Response
        if response.status_code == 204:
            print(f"Successfully Uploaded Image: [{image_path}]. ID is: [{upload_destination_id}]")
        else:
            print("Failed to upload Image.")
            print(response.text)
        return upload_destination_id


destination_id = ImageUploader().get_image_upload_destination_id(
    image_path="https://images.boxwave.com/products/amazon/bw-logo-600x180.jpg", is_web_request=True)

destination_id2 = ImageUploader().get_image_upload_destination_id(
    image_path="C:\\Users\\willb\\Desktop\\360_F_547856588_WTKqn3IcRZ2POen9mEbhXT27HobWhl67.jpg", is_web_request=False)
