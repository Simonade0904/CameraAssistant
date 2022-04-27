from dis import dis


class Listing:
    def __init__(self,source,name,buying_type,price,url,img_url,time_remaining = None):
        self.name = name
        self.source = source
        self.buying_type = buying_type
        self.price = price
        self.url = url
        self.img_url = img_url #Turns out it cannot be reliably scraped. Do not use in main application.
        self.time_remaining = time_remaining

    def __str__(self):
        display_name = ''
        if len(self.name) > 50:
            display_name = self.name[:50] + '...'
        else:
            display_name = self.name

        display_time = '' if self.buying_type == 'buy-it-now' else f'Time remaining: {self.time_remaining} '

        return (display_name + '\n\t' + f'Price: ${self.price} ' + display_time + f'Source: {self.source}')

    def print_full(self):
        display_time = '' if self.buying_type == 'buy-it-now' else f'Time remaining: {self.time_remaining} '
        return (self.name+ '\n\t' + f'Price: ${self.price} ' + display_time + f'Source: {self.source}')