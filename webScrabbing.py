from bs4 import BeautifulSoup
import requests
res=requests.get('https://www.hubertiming.com/home')
content=BeautifulSoup(res.content,'html.parser')
# f=open("web.html",'w')
# f.write(str(content))

p=content.find_all("p")
print(p)

ah=content.find_all('a')
print(ah)
for i in a:
    print(i.get('hf'))