import requests
import csv
import lxml.html
import write
from lxml import etree
from urllib.parse import urlencode
url = " https://search.jd.com/Search?keyword=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&enc=utf-8&wq=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&pvid=4bcc317cbd784c78af04dd25bc51cf6f"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.raise_for_status()
response.encoding = 'utf-8'
data = response.text
s = etree.HTML(data)
datas = s.xpath('//div[@id="J_goodsList"]/ul/li')

with open('JD_book.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['书名','价格','出版社'])
    writer.writeheader()
    Re=dict()
    for data in datas:
        name = data.xpath('div/div[@class="p-name"]/a/em/text()')
        price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
        shop = data.xpath('div/div[@class="p-shopnum"]/a/@title')
        write.writerow([name,price,shop])
    for i in range(len(name)):
        Re['书名']=name[i].strip()
        Re['价格']=price[i].strip()
        Re['出版社']=shop[i].strip()
        writer.writerow(Re)
f.close()
