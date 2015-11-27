
from logging import getLogger
from lxml import html
from os.path import exists, join
from os import makedirs
import requests
from urllib import urlretrieve

logger = getLogger(__name__)


def get_filename_from_url(url_string):
    return url_string[url_string.rfind('/')+1:]


def scrap_files_from_webpage(destination_path, url_string, xpath_selector_string):

    logger.info("Scraping: %s", url_string)
    logger.info("XPath Selector: %s", xpath_selector_string)
    logger.info("Destination: %s", destination_path)

    page = requests.get(url_string)
    tree = html.fromstring(page.content)
    file_uris = tree.xpath(xpath_selector_string)#'//meta[@property="og:image"]/@content')

    print file_uris

    if not exists(destination_path):
        try:
            logger.info("Destination doesn't exist, creating.")
            makedirs(destination_path)
        except (IOError, OSError) as e:
            logger.exception(e)
            exit()

    for file_uri in file_uris:
        filename = join(destination_path, get_filename_from_url(file_uri))
        logger.info("Downloading %s -> %s", file_uri, filename)
        urlretrieve(file_uri, filename)

