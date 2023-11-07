import requests
import openpyxl as ox
from bs4 import BeautifulSoup as BS

url = 'https://www.amazon.com/Best-Sellers/zgbs'
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'})

soup = BS(response.text, 'lxml')
data = []
# ищет название карточки
for i in soup.find_all("div", class_="zg-carousel-general-faceout"):
    ashka = i.find_all("a", class_="a-link-normal")
    # print(ashka[1].find("span").find("div"))
    a = (ashka[1].find("span").find("div"))
    data.append(a.text)

wb = ox.Workbook()
ws = wb.worksheets[0]
for i, statN in enumerate(data):
    print(i, statN)
    ws.cell(row=i + 1, column=1).value = statN
wb.save('some.xlsx')
