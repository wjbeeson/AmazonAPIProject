import json
import requests
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
from botocore.credentials import ReadOnlyCredentials
from dotenv import load_dotenv
import os
from pathlib import Path
import argparse


# Load variables from .env file
dotenv_path = Path('env/.env')
load_dotenv(dotenv_path=dotenv_path)

# User-Configurable Variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
refresh_token = os.getenv('REFRESH_TOKEN')
aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_secret_key = os.getenv('AWS_SECRET_KEY')
aws_region = 'us-east-1'
service = 'execute-api'

# Step 1: Request Access Token
token_url = 'https://api.amazon.com/auth/o2/token'
token_data = {
    'grant_type': 'refresh_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
}
token_r = requests.post(token_url, data=token_data)
token = json.loads(token_r.text)['access_token']

# Step 2: Prepare and Sign the Request for A+ Content
method = 'GET'
host = 'sellingpartnerapi-na.amazon.com'
uri = '/aplus/2020-11-01/contentDocuments'  # Update to target the searchContentDocuments operation

# Update parameters as needed for the specific A+ Content request
params = {
    'marketplaceId': os.getenv('MARKETPLACE_ID'),
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
    print("Successfully accessed the A+ Content!")
    #print("Response details:")
    #print(json.dumps(response.json(), indent=4))
else:
    print("Failed to access A+ Content.")
    print(response.text)