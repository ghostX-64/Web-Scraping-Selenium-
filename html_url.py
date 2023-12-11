# my_file = open("all_links.txt", "r")
# data = my_file.read()
# data_into_list = data.split("\n")

# # Storing all the value in a file
# file = open("Blog_contenttt.txt", "w", encoding="utf-8")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
import time

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

f = open("b.html", "w", encoding='utf-8')
# get source code
driver.get("https://klaviyo.tech/auditing-and-replaying-billions-of-streaming-events-with-aws-athena-398ecc58a914?source=collection_archive---------0-----------------------")
time.sleep(2)
html = driver.page_source
f.write(html)
print(html)

# close web browser
