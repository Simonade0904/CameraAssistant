from ebaysdk.finding import Connection as finding

words = "Canon"
api = finding(appid = 'QingyiWa-CameraAs-SBX-cdc5804b1-f16d67c7', config_file=None)
api_request = {'keywords': words, "outputSelector": 'SellerInfo'}

response = api.execute('findItemsByKeywords',api_request)
print(response)
