import re
import logging

from locators.books_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:
    """
    Given one of the specific book devs, find the data in the book (book, content, tags)
    """

    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        # logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'Book: {self.title}, £{self.price}, status: {self.status}, link: {self.link}'

    def __str__(self):
        return f'{self.title}, £{self.price}, ({self.rating} stars), {self.status}, link={self.link}'

    @property
    def title(self):
        logger.debug('Finding book title')
        locator = BookLocators.TITLE
        title = self.parent.select_one(locator).attrs["title"]
        logger.debug(f'Found book title `{title}`')
        return title

    @property
    def link(self):
        logger.debug('Finding book link')
        locator = BookLocators.TITLE
        link = self.parent.select_one(locator).attrs["href"]
        logger.debug(f'Found book link `{link}`')
        return link

    @property
    def price(self):
        logger.debug('Finding book price')
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f"Found book price `{float_price}'")
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating')
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found book rating `{rating_number}`')
        return rating_number

    @property
    def status(self):
        logger.debug('Finding book status')
        locator = BookLocators.STATUS
        status = self.parent.select_one(locator).text.strip()
        logger.debug(f'Found status `{status}`')
        return status
