from bs4 import BeautifulSoup
import requests
import pandas as pd

DD=[]
name=input('enter name = ')
n=int(input('enter n = '))
for i in range(1,n+1):
    url=BeautifulSoup(f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}",'html.parser')
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'lxml')

    Electronic=soup.find_all("div",class_="_3pLy-c row")
    for electric in Electronic:
        ename=electric.find("div",class_="_4rR01T").text    
        price=electric.find("div",class_="_30jeq3 _1_WHN1").text.replace("₹","")
        star=electric.find("div",class_="_3LWZlK").text
        rating_reviews=electric.find("span",class_="_2_R_DZ").text

        commonclass=electric.find_all("li",class_="rgWa7D")
        processors=[]
        ram=[]
        os=[]
        storage=[]
        inches=[]
        warranty=[]
        for i in range(0,len(commonclass)):
            p=commonclass[i].text
            if "Core" in p:
                processors.append(p)
            elif "RAM" in p:
                ram.append(p)
            elif "Operating" in p:
                os.append(p)
            elif "SSD" in p or "HDD" in p:
                storage.append(p)
            elif "Display" in p:
                inches.append(p)
            elif "Warranty" in p:
                warranty.append(p)
              
        b={
            "Name ": ename,
            "Price ": price,
            "Star " : star,
            "Rating " : rating_reviews,
            "Processor ": processors,
            "RAM" : ram,
            "Operating System":os,
            "Storage":storage,
            "Display":inches,
            "Warranty":warranty
            
        }
        DD.append(b)
       

df=pd.DataFrame(DD)
df.to_csv('Multiple_datas.csv')
print(df)
