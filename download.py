# save https://www.ssd.noaa.gov/PS/TROP/TCFP/data/ as an html file to /media/db/76C020A1C0206997/j/downloads/new/JRPdata/tcfp/
import os
import re
import requests
from bs4 import BeautifulSoup

# Load the HTML file
with open('/media/db/76C020A1C0206997/j/downloads/new/JRPdata/tcfp/Index of _PS_TROP_TCFP_data.html', 'r') as f:
    html = f.read()

# Parse the HTML file
soup = BeautifulSoup(html, 'html.parser')

# Find all links that match the specific format and end with .DAT
links = [a['href'] for a in soup.find_all('a', href=True) if re.match(r'^TCFP\d{10}\.DAT$', a['href'])]

# Prune links that are already downloaded
data_dir = '/media/db/76C020A1C0206997/j/downloads/new/JRPdata/tcfp/data'
downloaded_files = os.listdir(data_dir)
links = [link for link in links if link not in downloaded_files]

# Write the list of full links to a text file
base_url = 'https://www.ssd.noaa.gov/PS/TROP/TCFP/data/'
with open('links_full.txt', 'w') as f:
    for link in links:
        f.write('url = ' + base_url + link + '\n')
        f.write('output = data/' + link + '\n')

# Now you can use the command:
curl_cmd = '/home/db/local/curl/bin/curl -K links_full.txt --rate 10/m -s'
os.system(curl_cmd)
