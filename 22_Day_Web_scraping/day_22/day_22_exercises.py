import requests
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
status = response.status_code
print(status)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.body)