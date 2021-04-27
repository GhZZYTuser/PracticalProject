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