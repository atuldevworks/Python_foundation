from bs4 import BeautifulSoup as bs


htmlSample=open('Section11/001.html','r').read()




pritified_Data=bs(htmlSample,"html.parser")
print(pritified_Data.find('h1').string)


list_items=pritified_Data.find_all('li')

for i in list_items:
    print(i.string)
    
    
subtitleCapture=pritified_Data.find(name='p',attrs={'class':'subtitle'})
print(subtitleCapture.string)

paraghraph=[p for p in pritified_Data.find_all('p') if 'subtitle' not in p.attrs.get('class',[])]
print(paraghraph[0].string)