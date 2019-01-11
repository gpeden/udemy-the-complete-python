import re
from bs4 import BeautifulSoup


import logging

from locators.books_pages_locators import AllBooksPagesLocators
from parsers.book import BookParser


logger = logging.getLogger("scraping.all_books_page")


class AllBooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        logger.debug(f'Finding all books in page using `{AllBooksPagesLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(AllBooksPagesLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPagesLocators.PAGES).string.strip()
        logger.debug(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages

    
