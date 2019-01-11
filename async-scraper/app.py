import asyncio
import aiohttp
import async_timeout
import time
import requests
import logging

from pages.books_page import AllBooksPage
loop = asyncio.get_event_loop()

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ])

logger = logging.getLogger('scraping')

logger.debug("Loading books list...")

page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = AllBooksPage(page_content)

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'{response.status}: Page took {time.time() - page_start} : url = {url}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [f'http://books.toscrape.com/catalogue/page-{page_num}.html' for page_num in range(1, page.page_count)]


start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took {time.time() - start}')

for page_content in pages:
    logger.debug("Creating AllBooksPage from content")
    page = AllBooksPage(page_content)
    books.extend(page.books)
