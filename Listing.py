class Listing:
    def __init__(self,source,name,buying_type,price,url,img_url,time_remaining = None):
        self.name = name
        self.source = source
        self.buying_type = buying_type
        self.price = price
        self.url = url
        self.img_url = img_url
        self.time_remaining = time_remaining

    def __str__(self):
        return self.description[:20]