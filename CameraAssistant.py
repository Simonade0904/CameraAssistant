from ScrapeGoodwill import gwScrape
import asyncio

result = asyncio.get_event_loop().run_until_complete(gwScrape())
print(result)