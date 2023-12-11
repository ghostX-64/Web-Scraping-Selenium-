# import pdfkit

# config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe") 
# pdfkit.from_file('Blogs_contenttt.html', 'Blogs_contenttt.pdf', configuration = config)

import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML
HTML('Seed Zeng_Auditing and replaying billions of streaming events with AWS Athena_blog.html').write_pdf('Seed Zeng.pdf')

