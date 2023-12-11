from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
import time
import pdfkit

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

# Read URLs from the file
with open('all_links.txt', 'r') as file:
    urls = file.read().splitlines()

# Process each URL
for url in urls:
    driver.get(url)

    # Allow some time for the page to load (you might need to adjust this)
    time.sleep(5)

    # Extract information
    author_element = driver.find_element(By.XPATH, '//a[@data-testid="authorName"]')
    author_name = author_element.text

    title_element = driver.find_element(By.TAG_NAME, 'h1')
    title = title_element.text

    claps_element = driver.find_element(By.CLASS_NAME, 'pw-multi-vote-count')
    claps = claps_element.text

    date_element = driver.find_element(By.XPATH, '//span[@data-testid="storyPublishDate"]')
    date = date_element.text

    content_element = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    content = content_element.get_attribute("outerHTML")
    
    contents_element = driver.find_element(By.CLASS_NAME, 'pw-post-body-paragraph')
    contents = content_element.find_elements(By.XPATH, "following-sibling::*")
    cont = ''.join([i.get_attribute("outerHTML") for i in contents])

    # Save content to a file (optional)
    with open(f'{author_name}_{title}_blog.html', 'w', encoding='utf-8') as file:
        file.write(f"<h1>{title}</h1><p>Author: {author_name}</p><p>Claps: {claps}</p><p>Date: {date}</p>{content}{cont}")

    # Convert HTML to PDF using pdfkit
    config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file(f'{author_name}_{title}_blog.html', f'{author_name}_{title}_blog.pdf', configuration=config)

# Close the WebDriver
driver.quit()
