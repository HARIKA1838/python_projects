import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3Dvivo")
print(response)

soup=BeautifulSoup(response.content,'html.parser')
print(soup)

names=soup.find_all('div',class_="KzDlHZ")
name=[]
for i in names:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_="XQDdHH")
rating=[]
for i in ratings:
    d=i.get_text()
    rating.append(d)
# print(rating)

images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images:
    d=i['src']
    image.append
# print(image)

df=pd.DataFrame()
# print(df)

df["Names"]=name
df["Prices"]=price
df["Ratings"]=rating
df["Images"]=image

print(df.to_csv("Mobiles.csv"))
