import requests
import logging

from pages.books_page import AllBooksPage

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

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    logger.debug("Creating AllBooksPage from content")
    page = AllBooksPage(page_content)
    books.extend(page.books)


