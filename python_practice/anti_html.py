# 5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
# the web, and prints it after stripping HTML tags.



import sys
import requests  # this is used for fetching information
from bs4 import BeautifulSoup # this is used to remove the tags

def remove_html_tags(content):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    return ''.join(text.strip().split()) # stripping the spaces





def main():
    
    url = input("Please enter the url...\n")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # checking for status if its okay then 200 else error would be raised
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


    html_content = response.text
    plain_text = remove_html_tags(html_content)
    print(plain_text)
    

if __name__ == "__main__":
    main()


