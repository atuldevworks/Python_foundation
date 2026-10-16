import requests
from fake_useragent import UserAgent
import bs4 as bs
import re 

headers={
'User-Agent': UserAgent () .random,
'Accept-Language': 'en-US, en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': "https://www.google.com"
}

data=requests.request(method='GET',url='https://books.toscrape.com').content

bsData=bs.BeautifulSoup(data,'html.parser')


locator='article.product_pod h3 a'
itemLink=bsData.select_one(locator)
itemName=itemLink.attrs.get('href')
print(itemName)


locator='article.product_pod p.price_color'
item_price=bsData.select_one(locator).string
pattern=r'£([0-9]+.[0-9]+)'
matcher=re.search(pattern,item_price)
print(float(matcher.group(1)))



locator='article.product_pod p.star-rating'

starRatingTag=bsData.select_one(locator)
# print(starRatingTag)

classes=starRatingTag.attrs.get('class')
print(classes)
ratingClasses=filter(lambda x:x!='star-rating',classes)
print(list(ratingClasses)[0])
