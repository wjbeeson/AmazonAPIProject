import json
import urllib.parse

import sp_api.api.upload
import os
import hashlib
import requests
import sp_api.base.helpers

def _generate_access_token():
    token_response = requests.post(
        "https://api.amazon.com/auth/o2/token",
        data={
            "grant_type":"refresh_token",
            "refresh_token": os.environ['REFRESH_TOKEN'],
            "client_id": os.environ['CLIENT_ID'],
            "client_secret": os.environ['CLIENT_SECRET']
        }
    )
    return token_response.json()['access_token']



