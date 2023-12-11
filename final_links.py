import requests
from bs4 import BeautifulSoup

f = open("all_links.txt", "w")

a = [2018,2019,2020,2021,2022,2023]     #For upcoming years you can add [2024,2025,....]
for i in a:
    url = f"https://klaviyo.tech/archive/{i}"
    print(url)
    
    url1 = f"{url}/01"
    r=requests.get(url1)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,"html.parser")
    links = soup.find_all("a", class_="button button--smaller button--chromeless u-baseColor--buttonNormal")
    for k in links:
        # Print in a file
        f.write(k["href"])
        f.write("\n")
        print(k["href"])   
    
    b= ["02","03","04","05","06","07","08","09","10","11","12"]
    for j in b:
        url2 = f"{url}/{j}"
        print(url2)
        r=requests.get(url2)
        r.raise_for_status()
        if (r.url) == (url):    ## If redirecting to the same url
            continue
        else:
            soup = BeautifulSoup(r.text,"html.parser")
            links = soup.find_all("a", class_="button button--smaller button--chromeless u-baseColor--buttonNormal")
            for k in links:
                # Print in a file
                f.write(k["href"])
                f.write("\n")
                print(k["href"])
f.close()