import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Define the URL
url = input("Enter the webpage here: ")

# Send a request to the URL and get the HTML content
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Create a directory to save the downloaded files
dirname = 'downloaded_files'
if not os.path.exists(dirname):
    os.makedirs(dirname)

# Find all image tags and download the images
for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url.startswith('http'):
        filename = os.path.join(dirname, img_url.split('/')[-1])
        filename = urllib.parse.quote(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(img_url).content)
            
# Find all link tags with "rel" attribute "stylesheet" and download the linked CSS files
for link in soup.find_all('link', rel='stylesheet'):
    link_url = link.get('href')
    if link_url.startswith('http'):
        filename = os.path.join(dirname, link_url.split('/')[-1])
        filename = urllib.parse.quote(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(link_url).content)
        link['href'] = filename

# Find all link tags and download the linked pages
for link in soup.find_all('a'):
    link_url = link.get('href')
    if link_url.startswith('http'):
        filename = os.path.join(dirname, link_url.split('/')[-1])
        filename = urllib.parse.quote(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(link_url).content)
            
# Find all link tags and save the links to a text file
with open(os.path.join(dirname, 'links.txt'), 'w') as f:
    for link in soup.find_all('a'):
        link_url = link.get('href')
        if link_url.startswith('http'):
            f.write(link_url + '\n')

# Save the HTML file
with open(os.path.join(dirname, 'index.html'), 'wb') as f:
    f.write(html)
