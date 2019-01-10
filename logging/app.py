import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger('books')

logger.info("this will not show")
logger.warning("this will.")

logger = logging.getLogger('books.database')
logger.warning("tested logger.")
