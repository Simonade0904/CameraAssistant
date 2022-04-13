import requests
from requests_oauthlib import OAuth2Session
import EbaySecrets
import webbrowser

scope = "https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly https://api.ebay.com/oauth/api_scope/buy.shopping.cart https://api.ebay.com/oauth/api_scope/buy.offer.auction https://api.ebay.com/oauth/api_scope/commerce.identity.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.email.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.phone.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.address.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.name.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.status.readonly https://api.ebay.com/oauth/api_scope/sell.finances https://api.ebay.com/oauth/api_scope/sell.item.draft https://api.ebay.com/oauth/api_scope/sell.payment.dispute https://api.ebay.com/oauth/api_scope/sell.item https://api.ebay.com/oauth/api_scope/sell.reputation https://api.ebay.com/oauth/api_scope/sell.reputation.readonly https://api.ebay.com/oauth/api_scope/commerce.notification.subscription https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"

client_id = EbaySecrets.EBAY_CLIENT_ID

oauth = OAuth2Session(client_id, scope = scope)

authorization_url = "https://auth.sandbox.ebay.com/oauth2/authorize?client_id=QingyiWa-CameraAs-SBX-cdc5804b1-f16d67c7&response_type=code&redirect_uri=Qingyi_Wang-QingyiWa-Camera-lmbck&scope=https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.order.readonly https://api.ebay.com/oauth/api_scope/buy.guest.order https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly https://api.ebay.com/oauth/api_scope/buy.shopping.cart https://api.ebay.com/oauth/api_scope/buy.offer.auction https://api.ebay.com/oauth/api_scope/commerce.identity.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.email.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.phone.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.address.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.name.readonly https://api.ebay.com/oauth/api_scope/commerce.identity.status.readonly https://api.ebay.com/oauth/api_scope/sell.finances https://api.ebay.com/oauth/api_scope/sell.item.draft https://api.ebay.com/oauth/api_scope/sell.payment.dispute https://api.ebay.com/oauth/api_scope/sell.item https://api.ebay.com/oauth/api_scope/sell.reputation https://api.ebay.com/oauth/api_scope/sell.reputation.readonly https://api.ebay.com/oauth/api_scope/commerce.notification.subscription https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"

# webbrowser.open(authorization_url)

# authorization_response = input("Please enter the full URL after successful authorization: ")

# http_headers = {"Content-Type": "application/x-www-form-urlencoded",
#     "Authorization": "Basic <B64-encoded_oauth_credentials>"}

# body = {"grant_type":"client_credentials","scope":scope}

token = oauth.fetch_token("https://api.sandbox.ebay.com/identity/v1/oauth2/token")

# ,
# authorization_response = authorization_response,
# headers=http_headers,
# include_client_id=True,
# scope = scope)
# client_secret = EbaySecrets.EBAY_CLIENT_SECRET,

response = oauth.get("https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=nikon")

print(response.text)