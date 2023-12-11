from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
import time, pdfkit, os
from weasyprint import HTML

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

# Opening the file containing all links to scrap
my_file = open("all_links.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

pdf_files = []
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

# Storing all the value in a file
# file = open("Blogs_contenttt.html", "w", encoding="utf-8")

for i in data_into_list:
    driver.get(i)
    time.sleep(3)   # After opening the link the page should wait for 2 sec to get completely load
    
    ## For getting article title
    title = driver.find_element(By.TAG_NAME, 'h1')
    title1 = title.text
    
    # print(f"Tilte of the article: {title.get_attribute('outerHTML')}")
    # file.write(f"Tilte of the article: {title.get_attribute('outerHTML')} \n")
    # file.write(title.get_attribute('outerHTML'))

    #Code to get only html for the required elements
    
    # ## For getting author name
    name = driver.find_element(By.XPATH, '//a[@data-testid="authorName"]')
    name1 = name.text
    # # print(f"Author Name: {name.text}")
    # file.write(f"Author Name: {name.text} \n")
    # file.write(name.get_attribute('outerHTML'))
    
    # ## For getting Date
    date = driver.find_element(By.XPATH, '//span[@data-testid="storyPublishDate"]')
    # # print(f"Date of published: {date.text}")
    # file.write(f"Date of published: {date.text} \n")
    # file.write(date.get_attribute('outerHTML'))
    
    # ## For getting the claps received on that article
    claps = driver.find_element(By.CLASS_NAME, 'pw-multi-vote-count')
    claps1 = claps.text
    # # print(f"Claps on the article: {claps.text}")
    # file.write(f"Claps on the article: {claps.text} \n")
    # file.write(claps.get_attribute('outerHTML'))
    
    # ## For getting blog content 1st paragraph
    content = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    co = content.get_attribute("outerHTML")
    # # print(f"Content of that article:{content.text}")
    # file.write(f"Content of that article: {content.text} \n")
    # file.write(content.get_attribute('outerHTML'))
    # # for i in content:
    # #     print(i.text)
    
    cont = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    # contents = cont.find_elements(By.XPATH,"following-sibling::*")
    # for i in contents:
    # #     # print(i.text)
    # #     file.write(f"{i.text} \n")
    #     file.write(i.get_attribute('outerHTML'))
    
    contents = cont.find_elements(By.XPATH, "following-sibling::*")
    contt = ''.join([i.get_attribute("outerHTML") for i in contents])
    
    temp_html_file = f'{name1}_{claps1}_blog.html'
    with open(temp_html_file, 'w', encoding='utf-8') as file:
        file.write(f"<h1>{title.text}</h1><p>Author: {name.text}</p><p>Claps: {claps.text}</p><p>Date: {date.text}</p>{co}{contt}")
        file.write("<style>img{width:600px;}/style>")
        
    pdf_file = f'{name1}_{claps1}_blog.pdf'
    
    HTML(temp_html_file).write_pdf(pdf_file)
        
    pdf_files.append(pdf_file)
    os.remove(temp_html_file)  # Remove the temporary HTML file after creating PDF
        
# HTML(pdf_files).write_pdf('all_blogs.pdf')
        
      
    # # Getting all the content inside a div
    # contents = driver.find_elements(By.CSS_SELECTOR, '.pw-post-body-paragraph')
    # # cnt = contents.find_elements(By.XPATH,"following-sibling::*")
    # for cntt in contents:
    #     file.write(f"{cntt.text} \n")
    
    # file.write("\n")
# file.close()
my_file.close()
driver.quit()