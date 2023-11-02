import json
import os
import shutil
from pathlib import Path
import requests
import sp_api.api
import sp_api.api.upload
import sp_api.base.helpers
from dotenv import load_dotenv

class ApiManager:
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
        self.key_map_path = "env/key_map.txt"
        self.key_map = self._load_asin_map()

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

    def _map_asin_to_content_ref_key(self, asin_code):
        content_ref_key = ""
        if not os.path.isfile(self.key_map_path):
            raise Exception("Key map file does not exist. Could not map new Asin")

        if not asin_code in self.key_map:
            content_ref_key = self._get_content_ref_id_from_asin(asin_code)
            self.key_map[asin_code] = content_ref_key
            with open(self.key_map_path, 'w') as file:
                file.write(json.dumps(self.key_map))
        else:
            content_ref_key = self.key_map[asin_code]

        return content_ref_key

    def _get_content_ref_id_from_asin(self, asin_code):
        # Step 1: Request Access Token
        token = self._generate_access_token()

        # Step 2: Prepare the Request for A+ Content
        method = 'GET'
        host = 'sellingpartnerapi-na.amazon.com'
        uri = '/aplus/2020-11-01/contentPublishRecords'  # Update to target the searchContentDocuments operation

        # Update parameters as needed for the specific A+ Content request
        params = {
            'marketplaceId': self.default_marketplace_id,
            'asin': asin_code,
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
        content_ref_key = ""
        # Step 4: Handle the Response
        if response.status_code == 200:
            content_ref_key = json.loads(response.content.decode())['publishRecordList'][0]['contentReferenceKey']
            print(f"Content Reference Key for Asin [{asin_code}]: [{content_ref_key}]")
        else:
            print("Invalid Asin Code.")
            print(response.text)
        return content_ref_key

    def _load_asin_map(self, reset=False):  # reset deletes all the asin maps
        key_map = {}
        if reset:
            os.remove(self.key_map_path)
        if os.path.isfile(self.key_map_path):
            with open(self.key_map_path, 'rb') as handle:
                try:
                    key_map = json.loads(handle.read())
                except ValueError as e:
                    raise Exception(f"{self.key_map_path} is not a valid JSON. Please edit or delete.")
        else:
            with open(self.key_map_path, "a") as file:
                file.write(json.dumps(key_map))

        return key_map

    def _create_upload_destination(self, image_path):
        # Step 1: Request Access Token
        token = self._generate_access_token()

        # Step 2: Prepare the Request for A+ Content
        method = 'POST'
        host = 'sellingpartnerapi-na.amazon.com'
        uri = '/uploads/2020-11-01/uploadDestinations/aplus/2020-11-01/contentDocuments'  # Update to target the searchContentDocuments operation
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

    def _upload_image_for_aplus_content(self, image_path):
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
    def get_image_upload_link(self, image_path):
        return self._upload_image_for_aplus_content(image_path)

    def get_aplus_content_doc(self, asin_code):
        # Step 1: Request Access Token
        token = self._generate_access_token()

        # Step 2: Prepare the Request for A+ Content
        method = 'GET'
        host = 'sellingpartnerapi-na.amazon.com'
        content_ref_key = self._map_asin_to_content_ref_key(asin_code)
        uri = f'/aplus/2020-11-01/contentDocuments/{content_ref_key}'  # Update to target the searchContentDocuments operation

        # Update parameters as needed for the specific A+ Content request
        params = {
            'contentReferenceKey': content_ref_key,
            'marketplaceId': self.default_marketplace_id,
            'includedDataSet': ["CONTENTS", "METADATA"],
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

        # Step 4: Handle the Response
        if response.status_code == 200:
            print(f"Content Reference Doc for Asin [{asin_code}] Successfully Fetched")
        else:
            print(f"Document Fetch Failed for Asin: [{asin_code}].")
            print(response.text)
        return response.json()['contentRecord']['contentDocument']

    def update_aplus_content_doc(self, asin_code, content_doc):
        content_ref_key = self._map_asin_to_content_ref_key(asin_code)
        node = sp_api.api.AplusContent(
            credentials=
            dict(
                refresh_token=os.environ['REFRESH_TOKEN'],
                lwa_app_id=os.environ['CLIENT_ID'],
                lwa_client_secret=os.environ['CLIENT_SECRET'],
                aws_secret_key=os.environ['AWS_SECRET_KEY'],
                aws_access_key=os.environ['AWS_ACCESS_KEY'],
                # role_arn=os.environ['']
            )
        )
        response_draft = node.update_content_document(
            contentReferenceKey=content_ref_key,
            marketplaceId=self.default_marketplace_id,
            body={'contentDocument': content_doc}
        )

        response_approval = node.post_content_document_approval_submission(
            contentReferenceKey=content_ref_key,
            marketplaceId=self.default_marketplace_id
        )

        return response_draft, response_approval