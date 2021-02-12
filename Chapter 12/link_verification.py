#!/usr/bin/env python3
# link_verification.py - it searches for a category of photos in Imgur and
# downloads all the resulting images.

import requests, bs4, logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s – %(levelname)s – %(message)s")
logging.disable(logging.CRITICAL)


def main():

    # URL - change as desired
    url = "https://www.yahoo.com/news"

    # Get the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    logging.info(f'Request to {url} successful.')

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find all the links
    links = soup.select('link')
    for link in links:
        try:
            href = link.get('href')
            res = requests.get(href)
            res.raise_for_status()
            print(f'Page validated: {href}...')
            logging.info(f'Request to {href} successful.')
        except Exception as err:
            print(f'{href} returned the following error: {err}')
            logging.info(f'Error - {href}: {err}')
    print('Done')


main()
