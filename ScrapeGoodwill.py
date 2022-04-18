from inspect import Attribute
import pyppeteer
import asyncio
from Listing import Listing
import re
from bs4 import BeautifulSoup as bs

GOODWILL_CACHE_NAME = 'goodwill.html'

async def gwScrape(term):
    allContentHTML = []
    browser = await pyppeteer.launch(headless=False)
    page = await browser.newPage()
    await page.goto(f'https://shopgoodwill.com/categories/listing?st={term}&sg=&c=&s=&lp=0&hp=999999&sbn=&spo=false&snpo=false&socs=false&sd=false&sca=false&caed=4%2F9%2F2022&cadb=7&scs=false&sis=false&col=1&p=1&ps=40&desc=false&ss=0&UseBuyerPrefs=true&sus=false&cln=1&catIds=&pn=&wc=false&mci=false&hmt=false&layout=grid',{'waitUntil':'networkidle0'})
    allContentHTML.append(await page.content())
    # for i in range(5):
    #     await page.click('.p-paginator-next')
    #     url = await page.evaluate("() => window.location.href")
    #     await page.goto(url,{'waitUntil':'networkidle0'})
    #     allContentHTML.append(await page.content())
    return allContentHTML

def generateGoodwillObj(term):
    page_list = asyncio.get_event_loop().run_until_complete(gwScrape(term))


    all_listings = []

    for page in page_list:

        soup = bs(page, 'html.parser')

        allListings = soup.find_all('div', class_ = 'item-col')

        for item in allListings:
            try:
                name = item.find('a', class_ = 'feat-item_name').text
                price = item.find('p', class_ = 'feat-item_price').text[2:]
                time_remaining_element = str(item.find_all('li', class_ = 'ng-star-inserted')[1])
                time_remaining = ' '.join(re.findall(r'(\d+\w)+',time_remaining_element)[2:4])
                url = item.find('a', class_ = 'feat-item_name').attrs['href']
                img_url = item.find('img', class_ = 'feat-item_img').attrs['src']
                all_listings.append(Listing("goodwill", name, "auction", price, url, img_url, time_remaining))
            except AttributeError as e:
                print(e)
                continue

    print(all_listings)
    print('hello')