
"""
This script is responsible for checking twitter for direct messages and putting the source/message on the queue.
"""

#!/usr/bin/env python

from argparse import ArgumentParser
from logging import basicConfig, getLogger, INFO, DEBUG
from logging.config import dictConfig
from web_scraper import scrap_files_from_webpage

logger = getLogger(__name__)


def get_args():
    parser = ArgumentParser(description='Image Scraper')
    parser.add_argument('url', help='The url to read')
    parser.add_argument('xpath', help='The xpath query.  If problems occur, try encapsulating in quotes.')
    parser.add_argument('-d', '--destination', default=".", help='The destination to save files to')
    parser.add_argument('-v', '--verbose', help='Verbose log output', default=False, action='store_true')
    return parser.parse_args()


def main():

    args = get_args()

    basicConfig(level=INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(levelno)s - %(message)s')

    if args.verbose:
        logger.setLevel(DEBUG)

    scrap_files_from_webpage(args.destination, args.url, args.xpath)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Cancelling...")
