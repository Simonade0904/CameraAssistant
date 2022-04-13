import requests
from requests.auth import HTTPBasicAuth

headers = {'x-api-key': '0p0s568g7faxozlky4tpg4gf'}
response = requests.get('https://openapi.etsy.com/v3/application/listings/active?limit=25', headers=headers)
print(response.text)