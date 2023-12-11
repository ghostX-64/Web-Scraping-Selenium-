# Web Scraping and Exploratory Data Analysis Showcase

## Overview

This repository showcases my proficiency in web scraping and exploratory data analysis (EDA) through the extraction and analysis of blog data from Medium and Klaviyo.tech websites. 
Utilizing Python, Selenium, and BeautifulSoup, the project demonstrates a comprehensive process of data acquisition, transformation, and synthesis.

## Data Collection Process

In the initial phase, BeautifulSoup (script: `final_links.py`) is used to extract all blog links from the Klaviyo.tech website. 
These links are stored in `all_links.txt`, setting the stage for subsequent scraping.

## Data Scraping and Conversion

The core of the project resides in `final_pro.py`, where Selenium systematically scrapes essential blog details, including title, author name, publication date, claps received, and a snapshot of content. 
Extracted data is dynamically synthesized into an HTML file.

For broader accessibility and portability, the HTML file is converted into a PDF using the WeasyPrint library. Post PDF generation, the intermediate HTML file is promptly deleted for a streamlined process.

## Data Aggregation

The project culminates by merging individual blog PDFs into a consolidated document using PyMuPDF, resulting in a single, comprehensive PDF named `combined.pdf`. 
This file encapsulates a cohesive representation of scraped blog data from Klaviyo.tech.

## Conclusion

This project not only demonstrates proficiency in web scraping techniques but also showcases the ability to seamlessly integrate various technologies for a coherent data analysis pipeline. 
The resulting `combined.pdf` serves as a testament to the successful amalgamation of extracted blog data into a consolidated and accessible format.
