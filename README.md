# web-scraper

Python-based web scraper that extracts data from web pages using the Beautiful Soup library. It fetches the HTML content of a web page, parses it, and extracts the desired data for further processing or storage.

## Installation

1. Clone the repository:
```
git clone https://github.com/kd9s0/web-scraper
```

2. Navigate to the project directory:
```
cd web-scraper
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```


## Usage

1. Open `main.py` and update the `url` variable with the URL of the web page you want to scrape.

2. Run the main script:
```
python main.py
```
The script will fetch the web page content, scrape the data, and store it a CSV file named `output.csv` in the `data/` directory.

3. Customize the scraping logic:
- Modify the `scraper.py` file to implement specific scraping logic. You can use the Beautiful Soup library to navigate the HTML structure and extract the desired data.

4. Customize the data storage:
- Modify the `output.py` file to store the data in a different format or to a different location.




