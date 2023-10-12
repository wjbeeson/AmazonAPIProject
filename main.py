from dotenv import load_dotenv
import os
from pathlib import Path
import sp_api.api
import json
from sp_api.api import *


class AplusContentManager():
    def __init__(self):

        dotenv_path = Path('env/.env')
        load_dotenv(dotenv_path=dotenv_path)

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
        self.marketplaceID = os.environ['MARKETPLACE_ID']
        """
        self.asin_dict = {}
        if os.path.isfile(os.environ['ASIN_MAP_LOC']):
            self.asin_dict = json.load(open(os.environ['ASIN_MAP_LOC']))
        else:
            self.refresh_asin_map()
        """

    def get_key_from_asin(self, asin_code):
        r = self.node.search_content_publish_records(asin=asin_code, marketplaceId=self.marketplaceID)
        return r.payload['publishRecordList'][0]['contentReferenceKey']

    """
    def refresh_asin_map(self):
        self.asin_dict = {}
        response = self.node.search_content_documents(marketplaceId=os.environ['MARKETPLACE_ID'])
        payload = response.payload['contentMetadataRecords']
        ids = []
        pass
        for item in payload:
            if item['contentMetadata']['badgeSet'] == ['STANDARD']:
                ids.append(item['contentReferenceKey'])
        print(f"{ids.__len__()} IDs Detected. Starting Asin Mapping.")
        for id in ids:
            asin = self.node.list_content_document_asin_relations(
                contentReferenceKey=id,
                marketplaceId=self.marketplaceID,
            ).payload['asinMetadataSet'][0]['asin']

            self.asin_dict[asin] = id
            print(f"{self.asin_dict.__len__()}/{ids.__len__()} mapped.")
        json.dump(self.asin_dict, open(os.environ['ASIN_MAP_LOC'], 'w'))
    """

    def get_aplus_content_doc(self, asin_code):
        response = self.node.get_content_document(
            contentReferenceKey=self.get_key_from_asin(asin_code),
            marketplaceId=self.marketplaceID,
            includedDataSet=["CONTENTS", "METADATA"]
        )
        return {"contentDocument": response.payload['contentRecord']['contentDocument']}

    def update_aplus_content_doc(self, asin_code, content_doc):
        pass
        response_draft = self.node.update_content_document(
            contentReferenceKey=self.get_key_from_asin(asin_code),
            marketplaceId=self.marketplaceID,
            body=content_doc
        )
        response_approval = self.node.post_content_document_approval_submission(
            contentReferenceKey=self.get_key_from_asin(asin_code),
            marketplaceId=self.marketplaceID
        )
        return response_draft, response_approval


user_asin_code = 'B0CJ3FY6S3'
manager = AplusContentManager()
content_doc = manager.get_aplus_content_doc(user_asin_code)
pass
response_draft, response_approval = manager.update_aplus_content_doc(user_asin_code, content_doc)
pass
