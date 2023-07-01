from bs4 import BeautifulSoup

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Implement your parsing logic here to extract specific data
    # ...

    # Return the extracted data
    return extracted_data
