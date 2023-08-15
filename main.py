import argparse
import logging
from scraper import scraper
from data import output

def main(url):
    # Set up logging
    logging.basicConfig(filename='scraping.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Fetch the web page content
    html_content = scraper.fetch_page(url)

    if html_content:
        try:
            # Scrape the data
            data = scraper.scrape_data(html_content)

            # Store the data
            output.save_data(data)
        except Exception as e:
            # Log any errors
            logging.error(f"Error scraping or saving data: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web Scraping Script')
    parser.add_argument('--url', required=True, help='URL of the web page to scrape')
    args = parser.parse_args()

    main(args.url)
