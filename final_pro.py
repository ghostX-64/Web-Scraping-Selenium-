from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
import time, pdfkit, os
from weasyprint import HTML

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

# Opening the file containing all links to scrap
my_file = open("all_links.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

for i in data_into_list:
    driver.get(i)
    time.sleep(3)   # After opening the link the page should wait for 2 sec to get completely load
    
    ## For getting article title
    title = driver.find_element(By.TAG_NAME, 'h1')
    title1 = title.text
    
    ## For getting author name
    name = driver.find_element(By.XPATH, '//a[@data-testid="authorName"]')
    name1 = name.text
    
    ## For getting date
    date = driver.find_element(By.XPATH, '//span[@data-testid="storyPublishDate"]')
    
    ## For getting the claps received on that article
    claps = driver.find_element(By.CLASS_NAME, 'pw-multi-vote-count')
    claps1 = claps.text
    
    ## For getting blog content 1st paragraph
    content = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    co = content.get_attribute("outerHTML")
    
    cont = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    contents = cont.find_elements(By.XPATH, "following-sibling::*")
    
    # try:
    #     separator_div = driver.find_element(By.XPATH, '//div[@role="separator"]')
    #     # Skip this div and move to the next one
    #     contents.remove(separator_div)
    # except NoSuchElementException:
    #     pass
    
    contt = ''.join([i.get_attribute("outerHTML") for i in contents])
    
    temp_html_file = f'{name1}_{claps1}_blog.html'
    with open(temp_html_file, 'w', encoding='utf-8') as file:
        file.write(f"<h1>{title.text}</h1><p>Author: {name.text}</p><p>Claps: {claps.text}</p><p>Date: {date.text}</p>{co}{contt}")
        file.write("<style>img{width:600px;}/style>")
        
    pdf_file = f'{name1}_{claps1}_blog.pdf'
    
    HTML(temp_html_file).write_pdf(pdf_file)

    os.remove(temp_html_file)  # Remove the temporary HTML file after creating PDF
    
my_file.close()
driver.quit()