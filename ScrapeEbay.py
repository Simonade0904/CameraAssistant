import pyppeteer
import asyncio
from Listing import Listing
import re
from bs4 import BeautifulSoup as bs

async def ebayScrape(brand):
    browser = await pyppeteer.launch(headless=True)
    page = await browser.newPage()
    await page.goto(f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={brand}+film+camera&_sacat=0&_ipg=240',{'waitUntil':'networkidle0'})
    ContentHTML = await page.content()
    return ContentHTML

def generateEbayObj(brand):
    page = asyncio.get_event_loop().run_until_complete(ebayScrape(brand))

    listingObjects = []

    soup = bs(page, 'html.parser')

    allListings = soup.find_all('li', class_ = 's-item')
    print(allListings)

    for item in allListings:
        try:
            name = item.find('h3', class_ = 's-item__title').text
            price = item.find('span', class_ = 's-item__price').text[1:]
            time_remaining_element = str(item.find('span', class_ = 's-item__time-left'))
            time_remaining = ' '.join(re.findall(r'(\d+\w)+',time_remaining_element))
            buying_type = 'buy-it-now' if time_remaining == '' else 'auction'
            url = item.find('a', class_ = 's-item__link').attrs['href']
            img_url = item.find('img', class_ = 's-item__image-img').attrs['src']
            listingObjects.append(Listing("ebay", name, buying_type, price, url, img_url, time_remaining))
        except AttributeError as e:
            print(e)
            continue

    return listingObjects