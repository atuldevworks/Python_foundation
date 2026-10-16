import requests
from fake_useragent import UserAgent




url='https://www.amazon.in/s?k=laptop&crid=2RRZTOILXFZO5&sprefix=laptop%2Caps%2C316&ref=nb_sb_noss_2'


headers={
'User-Agent': UserAgent () .random,
'Accept-Language': 'en-US, en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': "https://www.google.com"
}

urlData=requests.get(url,headers=headers).text
localpath='Section11/phb.html'
file=open(localpath,'w').write(urlData)

