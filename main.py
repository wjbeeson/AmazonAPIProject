from dotenv import load_dotenv
import os
from pathlib import Path
import sp_api.api
from utility import *
import json
from sp_api.api import *


class AplusContentManager():
    def __init__(self):
        self.node = sp_api.api.AplusContent(
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
        self.marketplace_id = os.environ['MARKETPLACE_ID']
        self.access_token = self.node.auth.access_token

    def _get_key_from_asin(self, asin_code):
        r = ""
        try:
            r = self.node.search_content_publish_records(asin=asin_code, marketplaceId=self.marketplace_id)
        except:
            raise Exception(f"Asin: [{asin_code}] does not exist.")
        else:
            return r.payload['publishRecordList'][0]['contentReferenceKey']

    def get_aplus_content_doc(self, asin_code):
        response = self.node.get_content_document(
            contentReferenceKey=self._get_key_from_asin(asin_code),
            marketplaceId=self.marketplace_id,
            includedDataSet=["CONTENTS", "METADATA"]
        )
        return {"contentDocument": response.payload['contentRecord']['contentDocument']}

    def update_aplus_content_doc(self, asin_code, content_doc):
        pass
        response_draft = self.node.update_content_document(
            contentReferenceKey=self._get_key_from_asin(asin_code),
            marketplaceId=self.marketplace_id,
            body=content_doc
        )
        response_approval = self.node.post_content_document_approval_submission(
            contentReferenceKey=self._get_key_from_asin(asin_code),
            marketplaceId=self.marketplace_id
        )
        return response_draft, response_approval
    def upload_new_image(self, image_path):
        if not os.path.isfile(image_path):
            raise Exception(f"Invalid Image Filepath: [{image_path}]")
        path = "/uploads/v1/uploadDestinations/aplus/2020-11-01/images"
        hash_md5 = sp_api.base.helpers.create_md5(image_path)
        content_type = f"image/{image_path.split(".")[image_path.split(".").__len__() - 1]}"

        # North America SP API endpoint (from https://developer-docs.amazon.com/sp-api/docs/sp-api-endpoints)
        endpoint = "https://sellingpartnerapi-na.amazon.com"

        # Downloading orders (from https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference#getorders)

        # the getOrders operation is a HTTP GET request with query parameters
        request_params = {
            "marketplaceIds": os.environ['MARKETPLACE_ID'],
            # US Amazon Marketplace ID (from https://developer-docs.amazon.com/sp-api/docs/marketplace-ids)
            "contentMD5": hash_md5,
            # "contentType": content_type
        }

        destination = requests.get(
            endpoint
            + path
            + "?"
            + urllib.parse.urlencode(request_params),  # encode query parameters to the URL
            headers={
                "x-amz-access-token": self.access_token,
                # access token from LWA, every SP API request needs to have this header
            },
        )
        pass
        # pretty print the JSON response
        print(json.dumps(destination.json(), indent=2))

        resource = "aplus/2020-11-01/contentDocuments"
        node = sp_api.api.Upload(
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
        node.marketplace_id = os.environ['MARKETPLACE_ID']

        result = sp_api.api.Upload.upload_document(
            self=node,
            resource=resource,
            file=image_path,
            content_type=content_type,
        )
        pass


# Setup Environment
dotenv_path = Path('env/.env')
load_dotenv(dotenv_path=dotenv_path)


user_asin_code = 'B0CJ3FY6S3'
manager = AplusContentManager()
manager.upload_new_image(image_path="C:/Users/willb/Desktop/example_logo.jpg")
pass
content_doc = manager.get_aplus_content_doc(user_asin_code)
response_draft, response_approval = manager.update_aplus_content_doc(user_asin_code, content_doc)
