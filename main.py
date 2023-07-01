from scraper import scraper
from data import output

def main():
    # Fetch the web page content
    url = 'https://uniswap.org'
    html_content = scraper.fetch_page(url)

    if html_content:
        # Scrape the data
        data = scraper.scrape_data(html_content)

        # Store the data
        output.save_data(data)

if __name__ == '__main__':
    main() 
