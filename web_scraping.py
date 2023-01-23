import requests;#web requests
from bs4 import BeautifulSoup as bs;#parse source code

user = input("Enter a github username: ");#username in url
url = f"https://github.com/{user}";#template for github profiles
r = requests.get(url);#request a url
soup = bs(r.content,"html.parser");#r is the reponse 200 = Access granted and .content is the html source code
img = soup.find("img",{"alt":"Avatar"})["src"];#tag, attribute,[select a specfic tag value];
print(img);
#14mins 27/05/2022