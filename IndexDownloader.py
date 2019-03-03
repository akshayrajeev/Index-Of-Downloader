from bs4 import BeautifulSoup
import requests
import wget

links = []
print("Enter 'Index Of' URL")
url = input()
#print("Enter The Path To Save Files")
#path = input()

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

for link in (soup.find_all('a')):
    links.append(link['href'])

for link in links:
    download_url = url + "/" + link
    wget.download(download_url)
