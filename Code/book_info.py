import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.com/Oxford-Textbook-Neuropsychiatry-Textbooks-Psychiatry/dp/0198757131/ref=sr_1_15?dchild=1&keywords=textbook&qid=1618601161&sr=8-15"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

page=requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find(id="a-size-base mediaTab_subtitle"))
