# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import json

def crawl(url, depth, max_depth=5, visited=set()):
    if depth > max_depth or url in visited:
        return {}
    
    visited.add(url)
    print(f"Crawling URL: {url} at depth {depth}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the text from the page
    text = ' '.join([p.text for p in soup.find_all('p')])
    
    # Find all sub-links
    sub_links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    
    data = {url: text}
    for sub_link in sub_links:
        data.update(crawl(sub_link, depth + 1, max_depth, visited))
        time.sleep(1)  # Be kind to the server and avoid overloading it
    
    return data

if __name__ == "__main__":
    start_url = 'https://docs.nvidia.com/cuda/'
    crawled_data = crawl(start_url, 0)
    with open('crawled_data.json', 'w') as f:
        json.dump(crawled_data, f)
