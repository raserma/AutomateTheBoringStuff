#!/usr/bin/env python3
# image_site_download.py - it searches for a category of photos in Imgur and
# downloads all the resulting images.

# Note: Hardest part was to find the right selector to download the image.

import requests, os, bs4, logging, sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s – %(levelname)s – %(message)s")
logging.disable(logging.CRITICAL)


def main():
    category = "dogs"

    # Get the search URL
    site = "https://imgur.com/"

    url = f'{site}search?q={category}'

    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    logging.info(f'Request to {url} successful.')

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Create the dir
    os.makedirs('imgur_photos', exist_ok=True)

    # Find the URL of the pictures
    cards = soup.select('.image-list-link > img')

    if len(cards) == 0:
        print('No results found.')
        sys.exit(0)

    # Limit the number of downloads
    num_downloads = min(5, len(cards))
    for i in range(num_downloads):
        # Download the image
        image_url = cards[i].get('src')
        card_url = f'https:{image_url}'
        print('Downloading image %s...' % card_url)
        res = requests.get(card_url)
        res.raise_for_status()
        logging.info(f'Request to {card_url} successful.')

        # Save the image
        image_file = open(os.path.join('imgur_photos', os.path.basename(card_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        logging.info(f'Image {card_url} downloaded')

    print('All images downloaded successfully.')


main()

