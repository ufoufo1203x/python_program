import requests
import re

def get_url(url):
    response = requests.get(url)
    html = response.text
    
    urls = re.findall(url, html)
    return urls

'Select URL for web site'
urls = get_url('')
print(urls)